import math
from typing import Tuple


def f(a: float) -> float:
    """
    Gleichung zur Bestimmung des Krümmungsradius a
    """
    return a * math.cosh(50 / a) - a - 10


def solver(a_min: float, a_max: float, tol: float = 1e-6) -> Tuple[float, int]:
    if f(a_min) * f(a_max) >= 0:
        raise ValueError("Ungültiges Intervall!")

    for i in range(1000):
        a_mid = (a_min + a_max) / 2

        if abs(f(a_mid)) < tol:
            return a_mid, i

        if f(a_min) * f(a_mid) < 0:
            a_max = a_mid
        else:
            a_min = a_mid

    return a_mid, i


def berechne_laenge(a: float) -> float:
    """
    Berechnet die Länge der Leitung
    """
    return 2 * a * math.sinh(50 / a)


def aufgabe9() -> None:
    a, it = solver(1, 100)

    laenge = berechne_laenge(a)

    print("Krümmungsradius a:", a)
    print("Iterationen:", it)
    print("Länge der Leitung:", laenge)


if __name__ == "__main__":
    aufgabe9()