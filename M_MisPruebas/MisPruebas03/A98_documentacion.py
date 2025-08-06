import math

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La longitud de la base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área calculada del rectángulo.

    Raises:
        ValueError: Si la base o la altura son números negativos.
    """
    if base < 0 or altura < 0:
        return 0
    return base * altura


print(help(list))
