import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes=[]
imcs=[]
classificaçoes=[]

def cal_imc (peso,altura):
    imc= peso/ (altura *altura)
    return imc

def  classifica_imc(imc):
     if imc < 18.5:
      return "Abaixo do peso ideal",
     elif imc <= 24.9:
      return "peso normal",
     elif imc <= 29.9:
      return "levimente acima do peso",
     elif imc <= 34.9:
      return"obesidade grau 1",
     elif imc <=39.9:
      return "obesidade grau 2",
 
     elif imc <=40.00:
      return "obesidade grau 3",
 

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("digite seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    

    resultado=cal_imc(peso,altura)
    classificaçao,= classifica_imc(resultado)
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)
    imcs.append(resultado)
    classificaçoes.append(classificaçao)    



# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i],sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print()

    print(f"o seu imc foi {imcs[i]:.2f}")
    print(f"a sua classificaçao foi", classificaçoes[i])
    