
import os
os.system ("cls")



def logo ():
    os.system("cls")
    print("========")
    print("==== SENAI ====")
    print("========")

def somar(a,b):

 return a + b

def subtrair(a,b):
    return  a - b


def multiplicar(a,b):
    multiplicação = a * b
    print(f"multiplicação {multiplicação}")

def dividir(a,b):
    return a / b


logo()
print("=SOLICITANDO DADOS= ")
n1=int(input("digite o primeiro numero: "))
n2=int(input("digite o segundo numero: "))

soma=somar(n1,n2)
subtração = subtrair(n1,n2)
divisão = dividir(n1,n2)


logo()
print("=EXIBINDO RESULTADOS")
print(f"soma: {soma}")
print(f"subtração {subtração}")
print(f"divisão {divisão}")
multiplicar(n1,n2)