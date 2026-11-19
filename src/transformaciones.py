import pandas as pd


def transformar_datos(datos):
    """
    Aplica transformaciones para preparar
    el dataset para su posterior analisis.
    """

    datos_transformados = datos.copy()

    # 1. Convertir toneladas a tipo numerico
    datos_transformados["toneladas"] = pd.to_numeric(
        datos_transformados["toneladas"],
        errors="raise"
    )

    # 2. Crear una variable de periodo
    datos_transformados["periodo"] = pd.to_datetime(
        datos_transformados["año"].astype(str)
        + "-"
        + datos_transformados["mes"].astype(str)
        + "-01",
        format="%Y-%m-%d",
        errors="raise"
    )

    # 3. Crear una variable auxiliar para region
    datos_transformados["region_analisis"] = (
        datos_transformados["region"].fillna(
            "Extranjero / sin region chilena"
        )
    )


    # 4. Identificar registros del periodo de estudio
    datos_transformados["periodo_estudio"] = (
        datos_transformados["año"].between(2016, 2025)
    )

    return datos_transformados