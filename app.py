"""AquaSafe — Dashboard del Avance 4. Ejecutar: streamlit run app.py"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from src.proyecciones import preparar_serie_anual, proyectar_lineal, proyectar_media_movil


def formato_toneladas(valor):
    """Muestra millones para cantidades grandes y toneladas para cantidades pequeñas."""
    if abs(valor) >= 1_000_000:
        return f"{valor / 1_000_000:,.2f} M t"
    return f"{valor:,.2f} t"


st.set_page_config(page_title="AquaSafe | Desembarques", page_icon="🐟", layout="wide")
st.title("🐟 AquaSafe · Exploración y proyección")
st.caption("Desembarques pesqueros y acuícolas · SERNAPESCA · Período de estudio 2016–2025")
st.write("¿Qué especies presentan mayores aumentos o disminuciones en toneladas entre 2016 y 2025 y cómo varían entre regiones?")

RUTA_DATOS = Path(__file__).resolve().parent / "datos" / "procesados" / "dataset_limpio.csv"

@st.cache_data(show_spinner="Cargando datos procesados…")
def cargar_dataset(ruta):
    datos = pd.read_csv(ruta, encoding="utf-8-sig", low_memory=False)
    columnas = {"año", "region_analisis", "especie", "toneladas", "periodo_estudio"}
    faltantes = columnas - set(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas: {', '.join(sorted(faltantes))}")
    datos["año"] = pd.to_numeric(datos["año"], errors="raise").astype(int)
    datos["toneladas"] = pd.to_numeric(datos["toneladas"], errors="raise")
    datos = datos.loc[datos["año"].between(2016, 2025)].copy()
    return datos

if not RUTA_DATOS.exists():
    st.error("No se encontró datos/procesados/dataset_limpio.csv. Ejecuta primero: python main.py")
    st.stop()

try:
    df = cargar_dataset(str(RUTA_DATOS))
except (OSError, ValueError, KeyError) as exc:
    st.error(f"No fue posible cargar los datos: {exc}")
    st.stop()

st.sidebar.header("Filtros históricos")
periodo = st.sidebar.slider("Años de análisis", min_value=2016, max_value=2025, value=(2016, 2025))
regiones = ["Todas las regiones"] + sorted(df["region_analisis"].dropna().unique().tolist())
region = st.sidebar.selectbox("Región", regiones)
base = df if region == "Todas las regiones" else df.loc[df["region_analisis"] == region]
especies = ["Todas las especies"] + sorted(base["especie"].dropna().unique().tolist())
especie = st.sidebar.selectbox("Especie", especies)
filtrado = base if especie == "Todas las especies" else base.loc[base["especie"] == especie]
filtrado = filtrado.loc[filtrado["año"].between(*periodo)]

st.sidebar.header(" Parámetros de proyección")
horizonte = st.sidebar.slider("Años a proyectar", 1, 5, 3)
modelo = st.sidebar.selectbox("Método de proyección", ["Comparar ambos", "Regresión lineal", "Promedio móvil"])
ventana_max = min(5, periodo[1] - periodo[0] + 1)
ventana = st.sidebar.slider("Ventana del promedio móvil (años)", 2, max(2, ventana_max), min(3, max(2, ventana_max)), disabled=ventana_max < 2)

st.subheader("Indicadores dinámicos")
if filtrado.empty:
    st.warning("No hay registros para esta combinación de filtros. Prueba otra región, especie o período.")
    st.stop()

serie = preparar_serie_anual(filtrado, *periodo)
total = float(filtrado["toneladas"].sum())
promedio = float(serie.mean())
primero, ultimo = float(serie.iloc[0]), float(serie.iloc[-1])
variacion = (ultimo - primero) / primero * 100 if primero != 0 else None
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total desembarcado", formato_toneladas(total))
c2.metric("Promedio anual", formato_toneladas(promedio))
c3.metric("Variación (%)", f"{variacion:+.1f}%" if variacion is not None else "No calculable")
c4.metric("Registros", f"{len(filtrado):,}")
st.caption("M t = millones de toneladas; t = toneladas. El promedio se calcula sobre totales anuales, no sobre registros individuales. Los años sin registros en el filtro se muestran como 0.")

izq, der = st.columns(2)
with izq:
    st.subheader("Evolución histórica")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(serie.index, serie.values/1e6, marker="o", linewidth=2)
    ax.set(xlabel="Año", ylabel="Millones de toneladas")
    ax.grid(alpha=.25)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
with der:
    st.subheader("Histórico vs. proyección")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(serie.index, serie.values/1e6, "o-", label="Histórico", linewidth=2)
    proyecciones = {}
    if len(serie) >= 2:
        if modelo in ("Regresión lineal", "Comparar ambos"):
            proyecciones["Regresión lineal"] = proyectar_lineal(serie, horizonte)
        if modelo in ("Promedio móvil", "Comparar ambos"):
            proyecciones["Promedio móvil"] = proyectar_media_movil(serie, horizonte, ventana)
        for nombre, pred in proyecciones.items():
            ax.plot([int(serie.index[-1]), *pred.index], [ultimo/1e6, *(pred.values/1e6)], "--o", label=f"Proyección: {nombre}")
        ax.axvline(int(serie.index[-1]), linestyle=":", alpha=.6)
    else:
        st.info("Selecciona dos años o más para generar proyecciones.")
    ax.set(xlabel="Año", ylabel="Millones de toneladas")
    ax.legend(fontsize=8)
    ax.grid(alpha=.25)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

if proyecciones:
    st.subheader("Resultados proyectados (toneladas)")
    tabla = pd.DataFrame({nombre: s for nombre,s in proyecciones.items()})
    tabla.index.name = "Año futuro"
    st.dataframe(tabla.style.format("{:,.0f}"), use_container_width=True)

st.subheader(" Especies y regiones con más desembarques")
col1, col2 = st.columns(2)
with col1:
    especies_top = filtrado.groupby("especie")["toneladas"].sum().nlargest(10)/1e6
    st.caption("Top 10 de especies · millones de toneladas")
    st.bar_chart(especies_top, horizontal=True)
with col2:
    regiones_top = filtrado.groupby("region_analisis")["toneladas"].sum().nlargest(10)/1e6
    st.caption("Top 10 de regiones/categorías geográficas · millones de toneladas")
    st.bar_chart(regiones_top, horizontal=True)

st.info("Estas son proyecciones exploratorias, no pronósticos garantizados. No consideran cuotas, clima, esfuerzo pesquero, cambios normativos ni shocks ambientales. La regresión lineal limita valores negativos a 0; el promedio móvil utiliza predicciones anteriores para extender el horizonte. Los filtros con series muy escasas pueden producir proyecciones poco representativas.")