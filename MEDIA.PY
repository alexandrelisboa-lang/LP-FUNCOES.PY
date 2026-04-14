import os
os.system("cls")

def calcular_media(n1,n2):
    media = (n1+n2) / 2
    return media

def verificar_resultado(media):
 if media >=7:

    return "aprovado"

 else:
   return "reprovado"
 
while True:
 print ("solicitando dados")
 n1= int (input("digite a primeira nota:"))
 n2 = int(input("digite a segunda nota: "))
 if n1 and n2 > 10 or n1 and n2 < 0:
  print("opiçao invalida ")
 else:
  break

media= calcular_media(n1,n2)
resultado= verificar_resultado(media)

print("\n= exibindo resultado =")
print(f"media: {media}")
print(f"resultado:{resultado}")

