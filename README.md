
# Proyecto de Producción Pesquera y Acuícola

## Equipo AquaSafe - Grupo N°9

**Asignatura:** Programación Avanzada  
**Integrantes:** Denise Ñancucheo y Fedra Gotschlich  
**Docente:** Alex Flores Fuentealba  

## Descripción del proyecto

Este proyecto tiene como finalidad preparar y analizar datos históricos de desembarques pesqueros y acuícolas en Chile, utilizando Python y las bibliotecas Pandas, NumPy y Matplotlib.

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
|
|-- main.py
|-- README.md
|-- requirements.txt
|-- .gitignore
```

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib Pyplot
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

5. Ejecutar el programa:

```bash
python main.py
```

El programa utiliza el archivo original ubicado en:

`datos/originales/BD_desembarque.csv`

Al finalizar, genera:

`datos/procesados/dataset_limpio.csv`

Además, genera automáticamente las estadísticas, los indicadores y los gráficos correspondientes al avance 3.

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

Los módulos del avance 3 se encuentran integrados en `main.py`.

Al ejecutar el programa desde la carpeta principal, se generan automáticamente:

- `resultados/estadisticas.csv`
- `resultados/indicadores.csv`
- `resultados/graficos/grafico_01.png`
- `resultados/graficos/grafico_02.png`
- `resultados/graficos/grafico_03.png`

La ejecución automática fue comprobada desde la terminal de Visual Studio Code.

## Alcance

El proyecto permite preparar y analizar los datos históricos de desembarques pesqueros y acuícolas de Chile, identificando tendencias anuales, especies con mayores volúmenes y diferencias entre regiones.

Los análisis descriptivos realizados proporcionan una base para estudiar las variaciones de los desembarques durante el período 2016-2025.

La comparación específica de aumentos y disminuciones por especie dentro de cada región constituye una posible profundización del análisis.

## Estado del proyecto

El proyecto AquaSafe se desarrolló en tres etapas:

- **Avance 1:** Carga de datos, inspección inicial y diagnóstico de calidad del dataset.
- **Avance 2:** Limpieza, tratamiento de valores nulos, transformación y validación de los datos.
- **Avance 3:** Cálculo de estadísticas descriptivas, automatización de indicadores, generación de gráficos e interpretación de resultados.

El proyecto integra las tres etapas mediante un pipeline automatizado en Python, que permite procesar los datos y exportar los resultados en archivos CSV y PNG.

El repositorio incluye el código fuente, las dependencias, los resultados obtenidos y la documentación correspondiente.