def diagnosticar_rangos(datos):
    """
    Revisa posibles valores fuera de rango
    en el conjunto de datos.
    """

    print("\nDIAGNOSTICO DE RANGOS:")

    meses_invalidos = ~datos["mes"].between(1, 12)

    años_invalidos = ~datos["año"].between(2000, 2025)

    toneladas_negativas = datos["toneladas"] < 0

    print("Meses fuera de rango:", meses_invalidos.sum())
    print("Años fuera de rango:", años_invalidos.sum())
    print("Toneladas negativas:", toneladas_negativas.sum())



def diagnosticar_identificadores(datos):
    """
    Revisa si existen identificadores repetidos
    en el conjunto de datos.
    """

    print("\nDIAGNOSTICO DE IDENTIFICADORES:")

    ids_duplicados = datos["id"].duplicated().sum()

    print("Identificadores duplicados:", ids_duplicados)
    print("Identificadores diferentes:", datos["id"].nunique())



def validar_columnas(datos):
    """
    Comprueba que el dataset contenga
    las columnas necesarias para el proyecto.
    """

    columnas_esperadas = [
        "id", "año", "aguas", "region",
        "cd_puerto", "puerto_desembarque",
        "mes", "cd_especie", "especie",
        "toneladas", "tipo_agente"
    ]

    print("\nVALIDACION DE COLUMNAS:")

    faltantes = [
        columna for columna in columnas_esperadas
        if columna not in datos.columns
    ]

    if len(faltantes) == 0:
        print("Todas las columnas necesarias estan presentes.")
    else:
        print("Columnas faltantes:", faltantes)
        raise ValueError("El dataset no tiene todas las columnas requeridas.")

    print("\nTIPOS DE DATOS:")
    print(datos.dtypes)




    
    # Comprobar los tipos de datos necesarios
    from pandas.api.types import (
        is_integer_dtype,
        is_numeric_dtype,
        is_datetime64_any_dtype
    )

    print("\nVALIDACION AUTOMATICA DE TIPOS:")

    tipos_correctos = (
        is_integer_dtype(datos["año"])
        and is_integer_dtype(datos["mes"])
        and is_numeric_dtype(datos["toneladas"])
        and is_datetime64_any_dtype(datos["periodo"])
    )

    if tipos_correctos:
        print("Los tipos de datos principales son correctos.")
    else:
        raise TypeError("Se detectaron tipos de datos incorrectos.")

