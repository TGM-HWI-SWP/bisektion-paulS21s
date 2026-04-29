import matplotlib.pyplot as plt
import numpy as np


def f(x: float, n: float) -> float:
    return x**2 - n


def plotter(n: float) -> None:
    a: float = 0
    b: float = n

    x_vals = []
    error_vals = []

    for i in range(20):
        c: float = (a + b) / 2

        x_vals.append(c)
        error_vals.append(abs(f(c, n)))

        plt.clf()

        x = np.linspace(0, n + 5, 200)
        y = f(x, n)

        # Funktion
        plt.subplot(2, 1, 1)
        plt.plot(x, y)
        plt.axhline(0)
        plt.scatter(c, f(c, n))
        plt.title(f"Bisektion - Annäherung (n={n})")
        plt.xlabel("x")
        plt.ylabel("f(x)")

        # Fehler
        plt.subplot(2, 1, 2)
        plt.plot(range(len(error_vals)), error_vals)
        plt.title("Fehler pro Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("Fehler")

        plt.pause(0.3)

        if f(a, n) * f(c, n) < 0:
            b = c
        else:
            a = c

    plt.show()


def test_plotter() -> None:
    """
    Testet die Visualisierung mit den gleichen Werten wie Aufgabe 5
    """
    testwerte = [25, 81, 144]

    for n in testwerte:
        print(f"\nStarte Plot für n = {n}")
        plotter(n)


if __name__ == "__main__":
    test_plotter()
