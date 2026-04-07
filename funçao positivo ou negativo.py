import os 
os.system("cls")

def negativo(n1):
    if n1< 0:
        print(" o numero escolhido e negativo: ")

    else:
        print("o numero escolhido e positivo: ")


numero = int(input("digite um numero: "))   
negativo(numero)