import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz
import math

# Constantes
e = math.e
pi = math.pi
print(e)

# Entradas
expressao = input("Coloque a expressão que deseja integrar: ")
def f(x):
    return eval(expressao)

# funcao = lambda x: math.e**x
intervaloComeco  = float(input("Onde começa a integral? "))
intervaloFim  = float(input("Onde termina a integral? "))
numeroTrapezios = int(input("Coloque aqui o número de passos: "))

intervalos = np.linspace(intervaloComeco, intervaloFim, numeroTrapezios)

# Método para cálculo da área: 
def integralArea(f):
    integral = 0
    passo = intervalos[1]-intervalos[0]
    for i in range(len(intervalos)-1):
        integral = integral + 1/2*(f(intervalos[i])+f(intervalos[i+1]))*passo

    # Plotagem do gráfico da área
    x = np.linspace(1e-3, intervaloFim, 100)
    plt.plot(x, f(x), color="black")

    plt.ylim(0, 10)
    plt.xlim(0, 15)
    plt.ylabel("$f(x)$")
    plt.xlabel("$x$")
    plt.fill_between(x,intervaloComeco,f(x))
    plt.show()

    print(f"A integral numérica da expressão {expressao}, com intervalos de {intervaloComeco} a {intervaloFim} é {integral}")

def graficoFuncao(f):
    x = np.arange(-10, 10, 0.01)
    y = f(x)
    Y = cumtrapz(y, x, initial=0)

    plt.plot(x, y, label="f(x)= "+ expressao)
    plt.plot(x, x ** 3 / 3, label='F(x) = x³/3')
    plt.plot(x, Y, label="F(x)")
    plt.legend()
    plt.show()

def trapezios(f):
    x = np.linspace(1e-3,intervaloFim,100)
    plt.plot(x, f(x), "k--")

    plt.ylim(0, intervaloFim)
    plt.xlim(0, intervaloFim)

    plt.text(1.5, 0.1, "integral", fontsize=16, c="white")

    plt.ylabel("$f(x)$")
    plt.xlabel("$x$")

    for k in range(len(intervalos)-1):
        plt.fill_between([intervalos[k], intervalos[k+1]], 0, [f(intervalos[k]),f(intervalos[k+1])], color="C0")

    plt.show()

integralArea(f)
graficoFuncao(f)
trapezios(f)