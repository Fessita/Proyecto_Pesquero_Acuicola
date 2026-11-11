
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def generar_graficos(datos):
    """
    Genera tres graficos del desembarque pesquero
    durante el periodo 2016-2025.
    """

    # Crear carpeta de salida
    carpeta = Path("resultados/graficos")
    carpeta.mkdir(parents=True, exist_ok=True)

    # Seleccionar el periodo de estudio
    datos_estudio = datos.loc[
        datos["periodo_estudio"] == True
    ].copy()

    if datos_estudio.empty:
        raise ValueError(
            "No hay registros para generar los graficos."
        )

    # Configuracion general
    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 13,
        "axes.labelsize": 11
    })

    # =========================================
    # GRAFICO 1: EVOLUCION ANUAL
    # =========================================

    desembarque_anual = (
        datos_estudio.groupby("año")["toneladas"]
        .sum()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        desembarque_anual.index,
        desembarque_anual.values / 1_000_000,
        marker="o",
        linewidth=2,
        color="#6750A4",
        label="Desembarque anual"
    )

    ax.set_title(
        "Evolucion anual del desembarque pesquero (2016-2025)"
    )
    ax.set_xlabel("Año")
    
    ax.set_ylabel("Millones de toneladas desembarcadas")
    ax.ticklabel_format(axis="y", style="plain")

    ax.set_xticks(range(2016, 2026))
    ax.grid(alpha=0.3)
    ax.legend()

    fig.tight_layout()
    fig.savefig(
        carpeta / "grafico_01.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)

    # =========================================
    # GRAFICO 2: PRINCIPALES ESPECIES
    # =========================================

    especies = (
        datos_estudio.groupby("especie")["toneladas"]
        .sum()
        .nlargest(10)
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(11, 7))

    
    ax.barh(
        especies.index,
        especies.values / 1_000_000,
        color="#8D79C7"
    )


    ax.set_title(
        "Diez especies con mayor desembarque (2016-2025)"
    )
    ax.set_xlabel("Millones de toneladas desembarcadas")
    ax.set_ylabel("Especie")
    ax.grid(axis="x", alpha=0.3)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(
        carpeta / "grafico_02.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)

    # =========================================
    # GRAFICO 3: DESEMBARQUE POR REGION
    # =========================================

    regiones = (
        datos_estudio.groupby("region_analisis")["toneladas"]
        .sum()
        .sort_values()
    )

    fig, ax = plt.subplots(
        figsize=(12, max(6, len(regiones) * 0.45))
    )

    
    ax.barh(
        regiones.index,
        regiones.values / 1_000_000,
        color="#4C9F9B"
    )


    ax.set_title(
        "Desembarque por region o categoria geografica (2016-2025)"
    )
    
    ax.set_xlabel("Millones de toneladas desembarcadas")
    ax.set_ylabel("Region o categoria geografica")
    ax.grid(axis="x", alpha=0.3)
    ax.set_axisbelow(True)

    fig.tight_layout()
    fig.savefig(
        carpeta / "grafico_03.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)

    print("\nTres graficos generados correctamente.")
    print("Ubicacion:", carpeta)