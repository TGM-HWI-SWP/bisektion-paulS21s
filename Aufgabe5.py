
import math
from typing import Tuple, Optional


def f(x: float, n: float) -> float:
    """
    Berechnet den Funktionswert f(x) = x^2 - n.

    :param x: Eingabewert
    :param n: Konstante zur Wurzelberechnung
    :return: Funktionswert
    """
    return x**2 - n


def solver(n: float, tol: float = 1e-6, max_iter: int = 100) -> Optional[Tuple[float, int]]:
    """
    Bestimmt die Nullstelle der Funktion f(x) = x^2 - n
    mithilfe des Bisektionsverfahrens.

    :param n: Zahl, deren Wurzel berechnet wird
    :param tol: Toleranz für Abbruchbedingung
    :param max_iter: Maximale Anzahl an Iterationen
    :return: Tuple aus (Näherung; Iterationen) oder None bei Fehler
    """

    # Fehlerbehandlung: ungültige Eingabe
    if n < 0:
        print("Fehler: n muss >= 0 sein.")
        return None

    a: float = 0
    b: float = max(1, n)  # robustes Startintervall

    # Prüfen, ob Intervall gültig ist
    if f(a, n) * f(b, n) >= 0:
        print("Fehler: Es wurde kein gültiges Intervall gefunden.")
        return None

    # Bisektionsverfahren
    for i in range(max_iter):
        c: float = (a + b) / 2

        # Abbruchbedingung
        if abs(f(c, n)) < tol or abs(b - a) < tol:
            return c, i

        # Intervall halbieren
        if f(a, n) * f(c, n) < 0:
            b = c
        else:
            a = c

    # Wenn keine Konvergenz erreicht wurde
    print("WARNUNG: Maximale Iterationen erreicht.")
    return c, max_iter


def test_solver() -> None:
    """
    Testet den Solver für mehrere Werte und vergleicht
    die numerische Lösung mit der analytischen Lösung.
    """
    testwerte = [25, 81, 144]

    for n in testwerte:
        result = solver(n)

        if result is None:
            print(f"Test für n = {n} fehlgeschlagen.")
            continue

        approx, it = result
        exakt: float = math.sqrt(n)
        fehler: float = abs(approx - exakt)

        print(f"\nTest für n = {n}")
        print(f"Numerische Lösung : {approx:.6f}")
        print(f"Analytische Lösung: {exakt:.6f}")
        print(f"Fehler            : {fehler:.6e}")
        print(f"Iterationen       : {it}")


if __name__ == "__main__":
    test_solver()