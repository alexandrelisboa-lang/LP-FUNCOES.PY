import os 
os.system("cls")

#FUNÇAO COM PARAMETRO

def tabuada(numero):
     for i in range (1,11):
       print(f"{numero} x {i} = {numero * i}")


# EXEMPLO DE USO DA FUNÇAO. 
numero = int(input("digite um numero para tabuada: "))


# EXEMPLO A FUNÇAO 
# ENVIANDIO PARAMETRO
tabuada(numero)
