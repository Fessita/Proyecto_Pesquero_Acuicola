def limpiar_espacios(datos):
    """
    Elimina espacios innecesarios al inicio y al final
    de los valores de texto.
    """
    datos_limpios = datos.copy()

    for columna in datos_limpios.select_dtypes(include=["object"]).columns:
        datos_limpios[columna] = datos_limpios[columna].str.strip()

    cambios = 0

    for columna in datos.select_dtypes(include=["object"]).columns:
        original = datos[columna]
        limpio = datos_limpios[columna]

        diferencias = (
            original.ne(limpio)
            & original.notna()
            & limpio.notna()
        )

        cambios += int(diferencias.sum())

    print("Valores de texto corregidos:", cambios)

    return datos_limpios


def tratar_nulos(datos):
    """
    Conserva los valores nulos de region.
    Su relacion con puertos extranjeros
    se comprueba en las validaciones.
    """
    datos_limpios = datos.copy()

    nulos_iniciales = datos_limpios["region"].isna().sum()

    print("\nTRATAMIENTO DE VALORES NULOS:")
    print("Nulos iniciales en region:", nulos_iniciales)

    print("Estrategia: conservar los valores nulos")
    print("Justificacion: los registros sin region")
    print("corresponden a puertos extranjeros.")

    nulos_finales = datos_limpios["region"].isna().sum()

    print("Nulos finales en region:", nulos_finales)

    return datos_limpios