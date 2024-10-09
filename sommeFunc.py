def calculer_somme(liste):
    """
    Calcule la somme des éléments d'une liste et le nombre d'éléments.

    :param liste: Liste de nombres
    :return: Tuple contenant la somme des éléments et le nombre d'éléments
    """
    somme = sum(liste)
    nombre_elements = len(liste)
    return somme, nombre_elements