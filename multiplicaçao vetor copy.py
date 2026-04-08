import os

def logo():
    os.system("cls")
    print("========")
    print("==== SENAI ====")
    print("========")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b  

def dividir(a, b):
    if b == 0:
        return "Erro (Divisão por zero)"
    return a / b


logo()
print("= SOLICITANDO DADOS =")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


resultados = []

resultados.append(somar(n1, n2))
resultados.append(subtrair(n1, n2))
resultados.append(multiplicar(n1, n2))
resultados.append(dividir(n1, n2))

logo()
print("= EXIBINDO RESULTADOS =")

operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]

for i in range(len(resultados)):
    print(f"{operacoes[i]}: {resultados[i]}")