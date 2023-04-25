import math

# Entradas
expressao = input("Coloque a expressão que deseja integrar: ")
funcao = lambda x: eval(expressao)
erroEsperado = float(input("Coloque o erro desejado para integral: "))
intervaloComeco  = float(input("Onde começa a integral? "))
intervaloFim  = float(input("Onde termina a integral? "))
numeroTrapezios = 2

# Inicializando algumas variáveis que serão usadas durante o programa
erroAproximado = 100
numeroTrapezios = 1
valorAntigo = 0

# Caso o intervalo esteja invertido ou o usuário tenha colocado errado
if intervaloFim < intervaloComeco:
    print("o fim do intervalo é menor do que o começo, por favor, tente por novamente.")
    erroEsperado = float(input("Coloque o erro desejado para integral: "))
    intervaloComeco  = float(input("Onde começa a integral? "))
    intervaloFim  = float(input("Onde termina a integral? "))

# Mostrando as variáveis mudando durante as iterações: 
print("Número de Trapézios".ljust(25) + "Erro aproximado".ljust(25) + "Erro Real".ljust(25) + "integral".ljust(25))

while erroAproximado > erroEsperado:
    # Calculando o número de segmentos
    h = (intervaloFim-intervaloComeco)/numeroTrapezios

    # Calculando o termo de somatória
    soma = 0
    for j in range(1,numeroTrapezios):
        soma += 2 * funcao(intervaloComeco + j*h)
    
    # Calculando a estimativa da integral
    integral = (h/2) * (funcao(intervaloComeco) + soma + funcao(intervaloFim))

    # Retornando o erro aproximado e o erro real
    erroAproximado = abs(integral - valorAntigo)/integral * 100
    erroReal = abs(2.15888 - integral)/2.15888 * 100    

    # Guardando o valor da integral antiga
    valorAntigo = integral

    # Mostrando os valores a cada iteração
    print(f"{numeroTrapezios}".ljust(25) + f"{erroAproximado}".ljust(25) + f"{erroReal}".ljust(25) + f"{integral}".ljust(25))

    # Aumentando o número de trapézios
    numeroTrapezios += 1

print(f"A integral numérica da expressão {expressao}, com intervalos de {intervaloComeco} a {intervaloFim} é {integral:.8f}")