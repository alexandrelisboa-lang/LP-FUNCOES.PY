import os
os.system("cls")

def coversao(n1):
    return n1 * 100


print("====solicitando dados====")
num= int(input("digite o numero em metros para converte em centimetros: "))
multi= coversao(num)
print(f" a conversao e : {multi}")