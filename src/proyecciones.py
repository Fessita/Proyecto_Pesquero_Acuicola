"""Modelos simples de proyección anual de toneladas para AquaSafe."""
import numpy as np
import pandas as pd


def preparar_serie_anual(datos, inicio, fin):
    """Agrupa toneladas por año, incluyendo años sin registros como cero."""
    seleccion = datos.loc[datos["año"].between(inicio, fin)]
    serie = seleccion.groupby("año")["toneladas"].sum().reindex(
        range(inicio, fin + 1), fill_value=0.0
    ).astype(float)
    serie.index.name = "año"
    return serie


def proyectar_lineal(serie, horizonte):
    """Ajuste de mínimos cuadrados sobre totales anuales; no extrapola negativos."""
    if len(serie) < 2:
        raise ValueError("La regresión requiere al menos dos años históricos.")
    if horizonte < 1:
        raise ValueError("El horizonte debe ser positivo.")
    x = np.arange(len(serie), dtype=float)
    pendiente, intercepto = np.polyfit(x, serie.to_numpy(dtype=float), 1)
    futuros = np.arange(len(serie), len(serie) + horizonte, dtype=float)
    valores = np.maximum(pendiente * futuros + intercepto, 0)
    return pd.Series(valores, index=range(int(serie.index[-1]) + 1,
                                          int(serie.index[-1]) + horizonte + 1),
                     name="Regresión lineal")


def proyectar_media_movil(serie, horizonte, ventana):
    """Pronóstico iterativo: promedio de las últimas `ventana` observaciones."""
    if ventana < 2 or len(serie) < ventana:
        raise ValueError("La ventana debe ser al menos 2 y no exceder los años disponibles.")
    if horizonte < 1:
        raise ValueError("El horizonte debe ser positivo.")
    valores = list(serie.astype(float).to_numpy())
    predichos = []
    for _ in range(horizonte):
        siguiente = max(float(np.mean(valores[-ventana:])), 0.0)
        valores.append(siguiente)
        predichos.append(siguiente)
    return pd.Series(predichos, index=range(int(serie.index[-1]) + 1,
                                            int(serie.index[-1]) + horizonte + 1),
                     name="Promedio móvil")
