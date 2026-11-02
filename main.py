
from pathlib import Path
import pandas as pd

from src.carga import cargar_datos, inspeccionar_datos
from src.limpieza import limpiar_espacios, tratar_nulos
from src.transformaciones import transformar_datos
from src.validaciones import (
    diagnosticar_rangos,
    diagnosticar_identificadores,
    validar_columnas
)


def contar_fuera_de_rango(datos):
    """
    Cuenta registros con meses, años o toneladas
    fuera de los rangos revisados.
    """
    fuera_de_rango = (
        ~datos["mes"].between(1, 12)
        | ~datos["año"].between(2000, 2025)
        | (datos["toneladas"] < 0)
    )

    return int(fuera_de_rango.sum())


def main():
    # 1. CARGA DE DATOS
    ruta = "datos/originales/BD_desembarque.csv"
    datos = cargar_datos(ruta)

    if datos is None:
        print("No fue posible cargar el dataset.")
        return

    print("\nCARGA REALIZADA CORRECTAMENTE.")

    # 2. DIAGNOSTICO INICIAL
    print("\n=== DIAGNOSTICO INICIAL ===")
    inspeccionar_datos(datos)

    print("\nPORCENTAJE DE VALORES NULOS:")
    print((datos.isna().mean() * 100).round(4))

    print("\nCATEGORIAS ORIGINALES DE AGUAS:")
    print(datos["aguas"].value_counts(dropna=False))

    print("\nCATEGORIAS ORIGINALES DE TIPO DE AGENTE:")
    print(datos["tipo_agente"].value_counts(dropna=False))

    # 3. LIMPIEZA
    print("\n=== LIMPIEZA DE DATOS ===")
    datos_limpios = limpiar_espacios(datos)

    print("Limpieza de espacios ejecutada.")

    # 4. TRATAMIENTO DE NULOS
    print("\n=== TRATAMIENTO DE NULOS ===")
    datos_limpios = tratar_nulos(datos_limpios)

    # 5. TRANSFORMACIONES
    print("\n=== TRANSFORMACIONES ===")
    datos_transformados = transformar_datos(datos_limpios)

    print("Dimensiones:", datos_transformados.shape)

    print("\nCOLUMNAS NUEVAS:")
    print(
        datos_transformados[
            ["periodo", "region_analisis", "periodo_estudio"]
        ].head()
    )

    print("\nREGISTROS SEGUN PERIODO DE ESTUDIO:")
    print(
        datos_transformados["periodo_estudio"].value_counts()
    )

    # 6. VALIDACIONES FINALES
    print("\n=== VALIDACIONES FINALES ===")

    validar_columnas(datos_transformados)
    diagnosticar_rangos(datos_transformados)
    diagnosticar_identificadores(datos_transformados)

    nulos_region = datos_transformados["region"].isna()
    puerto_extranjero = (
        datos_transformados["puerto_desembarque"] == "Extranjero"
    )

    if not (nulos_region == puerto_extranjero).all():
        raise ValueError(
            "La relacion entre region faltante y puerto extranjero ha cambiado."
        )

    print("Correspondencia entre nulos y puertos extranjeros validada.")

    # 7. COMPARACION ANTES Y DESPUES
    print("\n=== COMPARACION ANTES Y DESPUES ===")

    # Contar cambios efectivos de tipo en columnas originales
    cambios_tipo = sum(
        datos[columna].dtype != datos_transformados[columna].dtype
        for columna in datos.columns
    )

    comparacion = pd.DataFrame({
        "Indicador": [
            "Filas",
            "Columnas",
            "Valores nulos",
            "Filas duplicadas",
            "Valores fuera de rango",
            "Variables transformadas (tipo)",
            "Variables nuevas"
        ],
        "Antes": [
            len(datos),
            len(datos.columns),
            int(datos.isna().sum().sum()),
            int(datos.duplicated().sum()),
            contar_fuera_de_rango(datos),
            0,
            0
        ],
        "Despues": [
            len(datos_transformados),
            len(datos_transformados.columns),
            int(datos_transformados.isna().sum().sum()),
            int(datos_transformados.duplicated().sum()),
            contar_fuera_de_rango(datos_transformados),
            cambios_tipo,
            len(datos_transformados.columns) - len(datos.columns)
        ]
    })

    print(comparacion.to_string(index=False))

    # 8. EXPORTACION
    print("\n=== EXPORTACION ===")

    ruta_salida = Path("datos/procesados/dataset_limpio.csv")
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    datos_transformados.to_csv(
        ruta_salida,
        index=False,
        encoding="utf-8-sig"
    )

    print("Dataset procesado exportado:", ruta_salida)

    # 9. VERIFICACION DEL ARCHIVO GENERADO
    datos_verificados = pd.read_csv(ruta_salida)

    print("\n=== VERIFICACION DEL CSV ===")
    print("Dimensiones:", datos_verificados.shape)
    print("Nulos:", datos_verificados.isna().sum().sum())
    print("Filas duplicadas:", datos_verificados.duplicated().sum())

    if datos_verificados.shape != datos_transformados.shape:
        raise ValueError(
            "Las dimensiones del archivo exportado no coinciden."
        )

    if int(datos_verificados.isna().sum().sum()) != int(
        datos_transformados.isna().sum().sum()
    ):
        raise ValueError(
            "Los valores nulos del archivo exportado no coinciden."
        )

    print("\nPIPELINE AQUASAFE FINALIZADO CORRECTAMENTE.")


if __name__ == "__main__":
    main()