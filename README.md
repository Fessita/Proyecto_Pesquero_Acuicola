# Proyecto de Producción Pesquera y Acuícola

## Equipo AquaSafe - Grupo N°9

**Asignatura:** Programación Avanzada  
**Integrantes:** Denise Ñancucheo y Fedra Gotschlich  
**Docente:** Alex Flores Fuentealba  

## Descripción del proyecto

Este proyecto tiene como finalidad preparar y analizar datos históricos de desembarques pesqueros y acuícolas en Chile, utilizando Python y las bibliotecas Pandas, NumPy, Matplotlib y Streamlit.

Se trabaja con información del Anuario Estadístico de Pesca y Acuicultura de SERNAPESCA, correspondiente al período 2000-2025.

## Pregunta del proyecto

¿Qué especies pesqueras y acuícolas presentan los mayores aumentos o disminuciones en las toneladas desembarcadas en Chile entre 2016 y 2025, y cómo varían estos cambios entre regiones?

## Objetivo general

Analizar la evolución histórica de los desembarques en Chile mediante Python y Pandas, para identificar variaciones en las toneladas registradas por especie, año y región.

## Fuente de datos

- Institución: Servicio Nacional de Pesca y Acuicultura (SERNAPESCA).
- Archivo: BD_desembarque.csv.
- Formato: CSV.
- Período: 2000-2025.
- Registros originales: 228.722.
- Columnas originales: 11.

Fuente:  
https://anuario.sernapesca.dataobservatory.net/desembarque/total

## Estructura del proyecto

```text
Proyecto_Pesquero_Acuicola/
|
|-- datos/
|   |-- originales/
|   |   |-- BD_desembarque.csv
|   |-- procesados/
|   |   |-- dataset_limpio.csv
|   |-- README_BD_desembarque.txt
|
|-- resultados/
|   |-- estadisticas.csv
|   |-- indicadores.csv
|   |-- graficos/
|       |-- grafico_01.png
|       |-- grafico_02.png
|       |-- grafico_03.png
|
|-- reportes/
|   |-- avance_1.pdf
|   |-- avance_2.pdf
|   |-- avance_3.pdf
|   |-- avance_4.pdf
|
|-- src/
|   |-- __init__.py
|   |-- carga.py
|   |-- limpieza.py
|   |-- transformaciones.py
|   |-- validaciones.py
|   |-- estadisticas.py
|   |-- indicadores.py
|   |-- visualizaciones.py
|   |-- proyecciones.py
|
|-- main.py
|-- app.py
|-- README.md
|-- requirements.txt
|-- .gitignore
```

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib Pyplot
- Streamlit
- Visual Studio Code
- GitHub

## Instalación y ejecución

1. Descargar o clonar el repositorio.

2. Abrir la carpeta del proyecto en Visual Studio Code.

3. Abrir una terminal desde la carpeta principal.

4. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

5. Ejecutar el programa principal:

```bash
python main.py
```

El programa utiliza el archivo original ubicado en:

`datos/originales/BD_desembarque.csv`

Al finalizar, genera:

`datos/procesados/dataset_limpio.csv`

Además, genera automáticamente las estadísticas, los indicadores y los gráficos correspondientes al Avance 3.

6. Para ejecutar el dashboard interactivo del Avance 4, utilizar:

```bash
python -m streamlit run app.py
```

Streamlit abrirá la aplicación en el navegador mediante una dirección local, generalmente:

`http://localhost:8501`

El dashboard utiliza el archivo `datos/procesados/dataset_limpio.csv`.

Si el archivo procesado todavía no existe, primero se debe ejecutar `python main.py`.

Para detener Streamlit, presionar `Ctrl + C` en la terminal.

## Funcionamiento del programa

El pipeline sigue las siguientes etapas:

1. Carga del archivo CSV con Pandas.
2. Diagnóstico inicial de calidad de los datos.
3. Limpieza de espacios innecesarios.
4. Tratamiento justificado de valores nulos.
5. Transformación de variables.
6. Validación de columnas, tipos y rangos.
7. Comparación de resultados antes y después.
8. Exportación y verificación del archivo procesado.
9. Cálculo de estadísticas descriptivas.
10. Cálculo de cinco indicadores automatizados.
11. Generación y exportación de tres gráficos con Matplotlib.

El Avance 4 incorpora una interfaz interactiva independiente del pipeline principal, permitiendo visualizar los datos históricos, aplicar filtros y calcular proyecciones futuras.

## Tratamiento de datos

Durante el diagnóstico se identificaron siete valores nulos en la variable `region`.

Se comprobó que corresponden a registros cuyo puerto figura como `Extranjero`. Por esta razón, se decidió conservarlos sin asignar una región chilena no verificada.

También se revisaron las categorías `NAC`, `Nac` y `AI` de la variable `aguas`. Se conservaron sus valores originales porque la documentación disponible no permite confirmar que las dos primeras sean equivalentes.

No se encontraron filas completamente duplicadas ni identificadores repetidos.

## Transformaciones aplicadas

- Conversión de `toneladas` a formato numérico.
- Creación de `periodo` a partir de año y mes.
- Creación de `region_analisis` para identificar registros sin región chilena.
- Creación de `periodo_estudio` para distinguir los registros de 2016-2025.

## Resultados del Avance 2

- Registros procesados: 228.722.
- Columnas finales: 14.
- Nuevas variables: 3.
- Valores nulos conservados: 7.
- Filas completamente duplicadas: 0.
- Registros eliminados: 0.

El archivo original se conserva sin modificaciones.

## Resultados del Avance 3

En esta etapa se incorporó el análisis estadístico y la visualización de los datos procesados en el avance anterior.

El análisis se concentra en el período 2016-2025, correspondiente a los últimos diez años disponibles en el dataset.

### Estadísticas descriptivas

Se implementó el módulo `estadisticas.py`, que permite calcular automáticamente:

- Cantidad de registros.
- Media.
- Mediana.
- Mínimo y máximo.
- Rango.
- Desviación estándar.
- Cuartiles.
- Frecuencias de variables categóricas.

Los resultados se exportan automáticamente en:

`resultados/estadisticas.csv`

**Resultados obtenidos:**

| Estadística | Resultado |
|---|---|
| Cantidad de registros | 93.816 |
| Media | 408,64 toneladas |
| Mediana | 9 toneladas |
| Mínimo | 1 tonelada |
| Máximo | 108.100 toneladas |
| Rango | 108.099 toneladas |
| Desviación estándar | 2.438,79 toneladas |
| Primer cuartil (25 %) | 2 toneladas |
| Segundo cuartil (50 %) | 9 toneladas |
| Tercer cuartil (75 %) | 69 toneladas |

La diferencia entre la media y la mediana muestra que los desembarques presentan una distribución desigual, donde algunos registros de mayor volumen elevan considerablemente el promedio.

### Indicadores automatizados

Se implementó el módulo `indicadores.py`, encargado de calcular cinco indicadores relacionados con el problema del proyecto:

1. Total de toneladas desembarcadas entre 2016 y 2025.
2. Promedio de toneladas por registro.
3. Especie con mayor volumen de desembarque.
4. Región con mayor volumen de desembarque.
5. Variación porcentual del volumen anual entre 2016 y 2025.

Los indicadores incluyen su método de cálculo, resultado e interpretación.

Los resultados se exportan automáticamente en:

`resultados/indicadores.csv`

**Resultados principales:**

| Indicador | Resultado |
|---|---|
| Total de toneladas desembarcadas | 38.337.005 toneladas |
| Promedio por registro | 408,64 toneladas |
| Especie con mayor desembarque | Salmón del Atlántico |
| Volumen de la especie principal | 7.073.785 toneladas |
| Región con mayor desembarque | Biobío |
| Volumen de la región principal | 11.224.630 toneladas |
| Variación porcentual 2016-2025 | +56,60 % |

Los resultados indican que el volumen anual registrado en 2025 fue superior al de 2016. Asimismo, permiten identificar las especies y regiones con mayor participación en el volumen acumulado del período.

### Visualización de datos

Se implementó el módulo `visualizaciones.py`, utilizando Matplotlib Pyplot para generar tres gráficos relacionados con la pregunta del proyecto.

**Gráfico 1: Evolución anual del desembarque pesquero (2016-2025)**

Archivo: `resultados/graficos/grafico_01.png`

Representa la evolución del volumen total desembarcado por año.

Se observa una tendencia general de crecimiento entre 2016 y 2025, con disminuciones puntuales durante algunos años del período.

**Gráfico 2: Diez especies con mayor desembarque (2016-2025)**

Archivo: `resultados/graficos/grafico_02.png`

Compara los volúmenes acumulados de las diez especies con mayor desembarque.

El salmón del Atlántico presenta el mayor volumen, seguido por el jurel y la anchoveta.

**Gráfico 3: Desembarque por región o categoría geográfica (2016-2025)**

Archivo: `resultados/graficos/grafico_03.png`

Compara los volúmenes acumulados de desembarque según región o categoría geográfica.

Las regiones de Biobío y Los Lagos presentan los mayores volúmenes, seguidas por Aysén.

Los tres gráficos incluyen títulos, nombres de los ejes y unidades expresadas en millones de toneladas para facilitar su interpretación.

### Automatización de resultados

Los módulos del Avance 3 se encuentran integrados en `main.py`.

Al ejecutar el programa desde la carpeta principal, se generan automáticamente:

- `resultados/estadisticas.csv`
- `resultados/indicadores.csv`
- `resultados/graficos/grafico_01.png`
- `resultados/graficos/grafico_02.png`
- `resultados/graficos/grafico_03.png`

La ejecución automática fue comprobada desde la terminal de Visual Studio Code.

## Avance 4: Dashboard interactivo y proyección de datos

En esta etapa se desarrolló una aplicación interactiva utilizando Streamlit, integrada con los datos previamente procesados por el equipo AquaSafe.

El objetivo del dashboard es permitir la exploración de los desembarques pesqueros y acuícolas entre 2016 y 2025, mediante filtros, indicadores dinámicos, visualizaciones y modelos matemáticos de proyección.

La aplicación permite analizar información histórica y explorar posibles comportamientos futuros sin necesidad de modificar el código fuente.

### Componentes implementados

**1. Filtros interactivos**

El dashboard incorpora tres filtros principales:

- Años de análisis: permite seleccionar un rango entre 2016 y 2025.
- Región: permite analizar una región específica o todas las regiones disponibles.
- Especie: permite seleccionar una especie pesquera o acuícola.

Los filtros modifican automáticamente los indicadores y las visualizaciones.

**2. Indicadores dinámicos**

Se implementaron cuatro indicadores:

- Total de toneladas desembarcadas.
- Promedio anual de toneladas desembarcadas.
- Variación porcentual entre los extremos del período seleccionado.
- Cantidad de registros filtrados.

Los indicadores se actualizan automáticamente al modificar los filtros.

Para facilitar la interpretación, las cantidades grandes se presentan en millones de toneladas, mientras que los valores pequeños se muestran directamente en toneladas.

Cuando el valor inicial de la serie es cero, la variación porcentual se presenta como "No calculable", evitando divisiones entre cero.

**3. Visualizaciones**

El dashboard presenta:

- Gráfico de evolución histórica de los desembarques.
- Gráfico comparativo entre datos históricos y proyecciones.
- Gráfico de las diez especies con mayor desembarque.
- Gráfico de regiones o categorías geográficas con mayor desembarque.

Las visualizaciones permiten identificar tendencias, fluctuaciones y diferencias entre especies y regiones.

**4. Tabla de resultados proyectados**

La aplicación genera una tabla que presenta las toneladas estimadas para cada año futuro según el modelo matemático seleccionado.

### Modelos matemáticos de proyección

Se implementó el módulo `src/proyecciones.py`, que contiene las funciones necesarias para preparar las series anuales y realizar las proyecciones.

Se incorporaron dos métodos matemáticos.

**Modelo 1: Regresión lineal**

La regresión lineal permite identificar una tendencia general utilizando los datos históricos.

Su expresión matemática es:

`y = mx + b`

Donde:

- `y`: toneladas estimadas.
- `x`: año analizado.
- `m`: pendiente de la tendencia.
- `b`: intercepto de la recta.

El modelo ajusta una línea a los datos históricos y utiliza esa tendencia para estimar los años posteriores.

Las predicciones negativas se limitan a cero porque no representan cantidades válidas de desembarque.

**Modelo 2: Promedio móvil**

El promedio móvil permite estimar valores futuros utilizando el promedio de una cantidad determinada de períodos anteriores.

Su expresión general es:

`P = (x1 + x2 + ... + xn) / n`

Donde:

- `P`: valor proyectado.
- `x`: toneladas correspondientes a períodos anteriores.
- `n`: cantidad de períodos considerados.

Este método permite suavizar las fluctuaciones de la serie histórica.

Para proyectar varios años, se incorporan las estimaciones anteriores en los cálculos sucesivos.

### Parámetros ajustables

El dashboard permite modificar:

1. **Horizonte de proyección:** entre 1 y 5 años futuros.
2. **Método de proyección:** regresión lineal, promedio móvil o comparación de ambos.
3. **Ventana del promedio móvil:** entre 2 y 5 períodos, según el rango histórico seleccionado.

Estos parámetros permiten explorar diferentes escenarios de proyección.

### Comparación de modelos

Como funcionalidad adicional, se implementó la comparación entre regresión lineal y promedio móvil.

El usuario puede seleccionar la opción "Comparar ambos" para visualizar simultáneamente los resultados.

En el gráfico comparativo se distinguen:

- Datos históricos.
- Proyección mediante regresión lineal.
- Proyección mediante promedio móvil.

Esta comparación permite analizar las diferencias entre una tendencia lineal y un método basado en promedios recientes.

### Resultados del dashboard

Para el período completo 2016-2025, considerando todas las regiones y especies, se obtuvieron aproximadamente:

| Indicador | Resultado |
|---|---|
| Total desembarcado | 38,34 millones de toneladas |
| Promedio anual | 3,83 millones de toneladas |
| Variación porcentual | +56,6 % |
| Registros analizados | 93.816 |

Al seleccionar un horizonte de cinco años, la aplicación permite calcular estimaciones desde 2026 hasta 2030.

**Resultados proyectados para 2030:**

| Método | Proyección |
|---|---|
| Regresión lineal | 5.058.629 toneladas |
| Promedio móvil (ventana de 5 años) | 4.248.398 toneladas |

Estos resultados corresponden a estimaciones matemáticas basadas en la información histórica seleccionada.

### Pruebas de funcionamiento

Se realizaron pruebas manuales del dashboard utilizando los datos procesados de AquaSafe.

Se comprobó que:

- La aplicación se ejecuta mediante Streamlit.
- Los filtros de año, región y especie actualizan los indicadores.
- Los gráficos históricos cambian al modificar los filtros.
- El horizonte temporal modifica los años proyectados.
- La ventana del promedio móvil modifica sus resultados.
- Los métodos de regresión lineal y promedio móvil pueden compararse visualmente.
- Las cantidades pequeñas se muestran en toneladas para evitar redondeos engañosos.
- La tabla de proyecciones presenta los resultados anuales correspondientes.

### Interpretación de resultados

Entre 2016 y 2025 se observa una tendencia general creciente en el volumen total de desembarques, aunque existen fluctuaciones durante distintos años.

La regresión lineal prolonga la tendencia histórica mediante una relación matemática entre el año y las toneladas desembarcadas.

El promedio móvil utiliza los valores de períodos anteriores, produciendo estimaciones más suavizadas.

Las diferencias entre los modelos muestran que los resultados futuros dependen del método matemático seleccionado y de los parámetros utilizados.

Por esta razón, las proyecciones deben interpretarse como escenarios exploratorios y no como valores futuros garantizados.

### Limitaciones

Los modelos empleados presentan las siguientes limitaciones:

- Utilizan información histórica y no incorporan todas las variables externas que pueden influir en la actividad pesquera.
- No consideran directamente cuotas de captura, condiciones climáticas ni cambios normativos.
- No incorporan posibles eventos ambientales extraordinarios.
- Las combinaciones de filtros con pocos registros pueden producir estimaciones poco representativas.
- Los resultados pueden variar según el período histórico y el método seleccionado.
- No se ha realizado una validación predictiva que permita garantizar la precisión futura de los modelos.

### Archivos incorporados

**`app.py`**

Contiene la interfaz interactiva desarrollada mediante Streamlit.

**`src/proyecciones.py`**

Contiene las funciones matemáticas utilizadas para preparar las series anuales y generar las proyecciones.

**`requirements.txt`**

Incorpora Streamlit junto con las bibliotecas utilizadas en las etapas anteriores.

## Alcance

El proyecto permite preparar y analizar los datos históricos de desembarques pesqueros y acuícolas de Chile, identificando tendencias anuales, especies con mayores volúmenes y diferencias entre regiones.

Los análisis descriptivos realizados proporcionan una base para estudiar las variaciones de los desembarques durante el período 2016-2025.

El dashboard amplía estas funcionalidades mediante herramientas interactivas que permiten seleccionar diferentes regiones, especies y períodos, así como explorar proyecciones matemáticas para años futuros.

La comparación específica de aumentos y disminuciones por especie dentro de cada región constituye una posible profundización del análisis.

## Estado del proyecto

El proyecto AquaSafe se desarrolló en cuatro etapas:

- **Avance 1:** Carga de datos, inspección inicial y diagnóstico de calidad del dataset.
- **Avance 2:** Limpieza, tratamiento de valores nulos, transformación y validación de los datos.
- **Avance 3:** Cálculo de estadísticas descriptivas, automatización de indicadores, generación de gráficos e interpretación de resultados.
- **Avance 4:** Desarrollo de un dashboard interactivo con filtros, indicadores automáticos, visualizaciones históricas, modelos matemáticos y parámetros ajustables.

El proyecto integra el procesamiento, análisis y visualización de datos mediante una arquitectura modular en Python.

El dashboard desarrollado en Streamlit permite explorar los resultados históricos y comparar escenarios futuros mediante regresión lineal y promedio móvil.

El repositorio contiene el código fuente, las dependencias, los resultados generados y la documentación de los avances realizados.