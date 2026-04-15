import os
os.system("cls")

# Função para limpar a tela
def limpar_tela():
    os.system("cls")

# Funções de Verificação (Retornam Booleano)
def eh_par(n):
    return n % 2 == 0

def eh_positivo(n):
    return n >= 0

# Variáveis globais
quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_impares = 0
quantidade_negativos = 0
quantidade_positivos = 0
soma_geral = 0
numeros = []
QUANTIDADE_N = 5

limpar_tela()

# Loop principal
for i in range(QUANTIDADE_N):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    soma_geral += num
    
    # Usando a função eh_par
    if eh_par(num):
        quantidade_pares += 1
        soma_pares += num
    else:
        quantidade_impares += 1
        soma_impares += num
        
    # Usando a função eh_positivo
    if eh_positivo(num):
        quantidade_positivos += 1
    else:
        quantidade_negativos += 1

# Saída de dados
limpar_tela()
print("=== Estatísticas dos Números ===")
print(f"Pares: {quantidade_pares} | Ímpares: {quantidade_impares}")
print(f"Positivos: {quantidade_positivos} | Negativos: {quantidade_negativos}")
print(f"Soma Geral: {soma_geral}")
print(f"Maior Número: {max(numeros)}")
print(f"Menor Número: {min(numeros)}")
print(f"Média: {soma_geral / QUANTIDADE_N:.2f}")
