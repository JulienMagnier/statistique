from statistics import mean

def calcul_moyenne(nombres):
    """
    Calcule la moyenne, le minimum et le maximum des éléments d'une liste.

    :param nombres: Liste de nombres
    :return: Tuple contenant la moyenne, le minimum et le maximum
    """ 

    moyenne = mean(nombres)
    min_val = min(nombres)
    max_val = max(nombres)

    return moyenne, min_val, max_val