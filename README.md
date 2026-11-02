
# Proyecto de Producción Pesquera y Acuícola

## Equipo AquaSafe - Grupo N°9

**Asignatura:** Programación Avanzada  
**Integrantes:** Denise Ñancucheo y Fedra Gotschlich  
**Docente:** Alex Flores Fuentealba  

## Descripción del proyecto

Este proyecto tiene como finalidad preparar y analizar datos históricos de desembarques pesqueros y acuícolas en Chile, utilizando Python y la biblioteca Pandas.

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

Proyecto_Pesquero_Acuicola/
- datos/
  - originales/
    - BD_desembarque.csv
  - procesados/
    - dataset_limpio.csv
  - README_BD_desembarque.txt
- reportes/
  - avance_1.pdf
  - avance_2.pdf
- src/
  - __init__.py
  - carga.py
  - limpieza.py
  - transformaciones.py
  - validaciones.py
- main.py
- README.md
- requirements.txt
- .gitignore

## Herramientas utilizadas

- Python
- Pandas
- Visual Studio Code
- Git y GitHub

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

## Alcance

El Avance 2 prepara los datos para su análisis posterior. La comparación de tendencias por especie y región y la interpretación de resultados corresponden a las siguientes etapas del proyecto.
