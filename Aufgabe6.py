import math
from typing import Tuple, Optional


def f(x: float, n: float) -> float:
    """
    Funktion f(x) = x^2 - n.
    """
    return x**2 - n


def df(x: float) -> float:
    """
    Ableitung f'(x) = 2x.
    """
    return 2 * x


def solver2(n: float, tol: float = 1e-6, max_iter: int = 100) -> Optional[Tuple[float, int]]:
    """
    Newton-Verfahren zur Berechnung der Wurzel von n.

    :param n: Zahl, deren Wurzel berechnet wird
    :param tol: Toleranz
    :param max_iter: maximale Iterationen
    :return: (Näherung, Iterationen) oder None bei Fehler
    """

    if n < 0:
        print("Fehler: n muss >= 0 sein.")
        return None

    x: float = max(1.0, n / 2)  # sinnvoller Startwert

    for i in range(max_iter):

        if abs(df(x)) < 1e-12:
            print("Fehler: Ableitung zu klein.")
            return None

        x_new: float = x - f(x, n) / df(x)

        # Abbruchbedingung
        if abs(x_new - x) < tol:
            return x_new, i

        x = x_new

    print("Warnung: Maximale Iterationen erreicht.")
    return x, max_iter


def test_solver2() -> None:
    """
    Testet das Newton-Verfahren mit den Werten aus Aufgabe 1, 2 und 5
    und vergleicht die numerische mit der analytischen Lösung.
    """
    testwerte = [17, 25, 81, 144]

    for n in testwerte:
        approx, it = solver2(n)
        exakt = math.sqrt(n)

        print(f"\nTest für n = {n}")
        print(f"Newton-Lösung     : {approx:.6f}")
        print(f"Analytische Lösung: {exakt:.6f}")
        print(f"Fehler            : {abs(approx - exakt):.6e}")
        print(f"Iterationen       : {it}")


if __name__ == "__main__":
    test_solver2()