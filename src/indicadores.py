
import pandas as pd
import numpy as np


def calcular_indicadores(datos):
    """
    Calcula cinco indicadores del desembarque pesquero
    durante el periodo de estudio 2016-2025.
    """

    # Seleccionar los registros del periodo de estudio
    datos_estudio = datos.loc[
        datos["periodo_estudio"] == True
    ].copy()

    if datos_estudio.empty:
        raise ValueError(
            "No existen registros para el periodo 2016-2025."
        )

    # 1. Total de toneladas desembarcadas
    total_toneladas = datos_estudio["toneladas"].sum()

    # 2. Promedio de toneladas por registro
    promedio_toneladas = datos_estudio["toneladas"].mean()

    # 3. Especie con mayor volumen desembarcado
    toneladas_especie = (
        datos_estudio.groupby("especie")["toneladas"]
        .sum()
        .sort_values(ascending=False)
    )

    especie_principal = toneladas_especie.index[0]
    total_especie = toneladas_especie.iloc[0]

    # 4. Region con mayor volumen desembarcado
    toneladas_region = (
        datos_estudio.groupby("region_analisis")["toneladas"]
        .sum()
        .sort_values(ascending=False)
    )

    region_principal = toneladas_region.index[0]
    total_region = toneladas_region.iloc[0]

    # 5. Variacion porcentual entre 2016 y 2025
    toneladas_anuales = (
        datos_estudio.groupby("año")["toneladas"].sum()
    )

    if 2016 not in toneladas_anuales.index:
        raise ValueError("No existen datos para el año 2016.")

    if 2025 not in toneladas_anuales.index:
        raise ValueError("No existen datos para el año 2025.")

    total_2016 = toneladas_anuales.loc[2016]
    total_2025 = toneladas_anuales.loc[2025]

    if total_2016 != 0:
        variacion = (
            (total_2025 - total_2016) / total_2016
        ) * 100
        resultado_variacion = round(variacion, 2)
    else:
        resultado_variacion = np.nan

    # Crear tabla de indicadores
    indicadores = [
        {
            "Indicador": "Total de toneladas desembarcadas",
            "Metodo de calculo": "Suma de toneladas (2016-2025)",
            "Resultado": round(total_toneladas, 2),
            "Interpretacion": (
                "Volumen total desembarcado durante "
                "el periodo de estudio."
            )
        },
        {
            "Indicador": "Promedio de toneladas por registro",
            "Metodo de calculo": "Media de toneladas",
            "Resultado": round(promedio_toneladas, 2),
            "Interpretacion": (
                "Cantidad promedio de toneladas "
                "por registro."
            )
        },
        {
            "Indicador": "Especie con mayor desembarque",
            "Metodo de calculo": "Suma de toneladas por especie",
            "Resultado": (
                f"{especie_principal}: "
                f"{total_especie:,.2f} toneladas"
            ),
            "Interpretacion": (
                "Especie que acumula el mayor volumen "
                "de desembarque durante el periodo."
            )
        },
        {
            "Indicador": "Region con mayor desembarque",
            "Metodo de calculo": "Suma de toneladas por region",
            "Resultado": (
                f"{region_principal}: "
                f"{total_region:,.2f} toneladas"
            ),
            "Interpretacion": (
                "Region o categoria geografica con "
                "el mayor volumen desembarcado."
            )
        },
        {
            "Indicador": "Variacion porcentual 2016-2025",
            "Metodo de calculo": (
                "((Total 2025 - Total 2016) / "
                "Total 2016) * 100"
            ),
            "Resultado": (
                f"{resultado_variacion:.2f}%"
                if pd.notna(resultado_variacion)
                else "No calculable"
            ),
            "Interpretacion": (
                "Cambio porcentual del volumen anual "
                "entre 2016 y 2025."
            )
        }
    ]

    return pd.DataFrame(indicadores)