import os 
os.system("cls")

def calcular_media (n1,n2):
    media = (n1+n2) / 2
    return media

def verificar_resultados(media):
    if media >=7:
        resultado = "Aprovado"

    else:
        resultado = "reprovado"
    return media

print (" = solicitanto dados =")
n1 =int(input("digite a primeira nota : "))
n2 = int(input("digite a segunda nota: "))

media = calcular_media(n1,n2)
resultado = verificar_resultados (media)


print("\n= exibindo resultado =")
print(f"media: {media}")
print(f"resultado:{resultado}")
