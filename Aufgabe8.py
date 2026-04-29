from typing import Tuple


def f(x: float) -> float:
    return 2*x + x**2 + 3*x**3 - x**4


def solver(a: float, b: float, tol: float) -> Tuple[float, int]:
    if f(a) * f(b) >= 0:
        raise ValueError("Ungültiges Intervall!")

    for i in range(1000):
        c = (a + b) / 2

        if abs(f(c)) < tol:
            return c, i

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, i


def test_aufgabe8() -> None:
    a = 3
    b = 4

    for tol in [1e-2, 1e-8]:
        x, it = solver(a, b, tol)

        print(f"\nToleranz: {tol}")
        print(f"Lösung: {x}")
        print(f"Iterationen: {it}")
        print(f"Fehler: {abs(f(x))}")


if __name__ == "__main__":
    test_aufgabe8()