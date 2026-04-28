
import os
usuarios = {}

def cria_usuario():
    nome = input("Escreva o nome do usuário: ")
    if nome in usuarios:
        print(" Usuário já existente!")
    else:
        email = input("Digite um e-mail: ") 
        senha = input("Digite uma senha: ")
        # Criamos um "dicionário dentro do dicionário" para salvar os dados
        usuarios[nome] = {"email": email, "senha": senha, "saldo": 0.0}
        print(f" Usuário {nome} criado com sucesso!")

def depositar():
    nome = input("Informe o nome do usuário para depósito: ")
    if nome in usuarios:
        valor = float(input("Digite o valor que você deseja depositar: R$ "))
        if valor > 0:
            usuarios[nome]["saldo"] += valor
            print(f" Depósito de R$ {valor:.2f} realizado!")
        else:
            print("Valor inválido.")
    else:
        print(" Usuário não encontrado.")

def sacar():
    nome = input("Informe o nome do usuário para saque: ")
    if nome in usuarios:
        valor = float(input("Digite o valor que você deseja sacar: R$ "))
        if 0 < valor <= usuarios[nome]["saldo"]:
            usuarios[nome]["saldo"] -= valor
            print(f" Saque de R$ {valor:.2f} realizado!")
        else:
            print(" Saldo insuficiente ou valor inválido.")
    else:
        print(" Usuário não encontrado.")

def ver_saldo():
    nome = input("Informe o nome do usuário: ")
    if nome in usuarios:
        saldo_atual = usuarios[nome]["saldo"]
        print(f" Saldo atual de {nome}: R$ {saldo_atual:.2f}")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        # Limpa a tela (opcional, dependendo do sistema)
        # os.system("cls" if os.name == "nt" else "clear")
        
        print("""
        ======= BANCO DO BICO =======
        1- CRIAR USUÁRIO
        2- DEPOSITAR
        3- SACAR
        4- VER SALDO
        5- SAIR
        =============================
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cria_usuario()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            ver_saldo()
        elif opcao == "5":
            print("Encerrando sistema... Até logo!")
            break
        else:
            print(" Opção inválida...")


if __name__ == "__main__":
    menu()