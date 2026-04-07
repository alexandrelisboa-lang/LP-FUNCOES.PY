import os 
os.system("cls")

def pares(n1):
    if n1 % 2 == 0 :
        print(" o numero escolhido e par.")

    else:
        print(" o numero escolhido e impar.")

numero = int(input("digite um numero: "))
pares(numero)