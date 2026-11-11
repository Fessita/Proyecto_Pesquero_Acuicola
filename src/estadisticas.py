
import pandas as pd
import numpy as np


def calcular_estadisticas(datos):
    """
    Calcula estadisticas descriptivas y frecuencias
    del desembarque pesquero durante 2016-2025.
    """

    # Seleccionar los ultimos diez años del estudio
    datos_estudio = datos.loc[
        datos["periodo_estudio"] == True
    ].copy()

    if datos_estudio.empty:
        raise ValueError(
            "No existen registros para el periodo 2016-2025."
        )

    # Variable principal: toneladas desembarcadas
    toneladas = pd.to_numeric(
        datos_estudio["toneladas"],
        errors="raise"
    ).dropna()

    if toneladas.empty:
        raise ValueError(
            "No existen valores validos de toneladas."
        )

    # Estadisticas descriptivas
    estadisticas = {
        "Cantidad de registros": len(datos_estudio),
        "Media (toneladas)": np.mean(toneladas),
        "Mediana (toneladas)": np.median(toneladas),
        "Minimo (toneladas)": np.min(toneladas),
        "Maximo (toneladas)": np.max(toneladas),
        "Rango (toneladas)": np.ptp(toneladas),
        "Desviacion estandar (toneladas)": np.std(
            toneladas, ddof=1
        ),
        "Cuartil 1 (25%)": np.percentile(toneladas, 25),
        "Cuartil 2 (50%)": np.percentile(toneladas, 50),
        "Cuartil 3 (75%)": np.percentile(toneladas, 75)
    }

    # Crear tabla de estadisticas
    tabla_estadisticas = pd.DataFrame(
        [
            {
                "Estadistica": nombre,
                "Valor": (
                    str(valor)
                    if nombre == "Cantidad de registros"
                    else f"{valor:.2f}"
                )
            }
            for nombre, valor in estadisticas.items()
        ]
    )

    # Calcular frecuencias de variables categoricas
    frecuencias = []

    for columna in ["especie", "region_analisis", "tipo_agente"]:
        conteo = datos_estudio[columna].value_counts(
            dropna=False
        )

        for categoria, cantidad in conteo.items():
            frecuencias.append({
                "Estadistica": (
                    f"Frecuencia {columna}: {categoria}"
                ),
                "Valor": str(int(cantidad))
            })

    tabla_frecuencias = pd.DataFrame(
        frecuencias,
        columns=["Estadistica", "Valor"]
    )

    # Unir estadisticas y frecuencias
    resultado = pd.concat(
        [tabla_estadisticas, tabla_frecuencias],
        ignore_index=True
    )

    return resultado