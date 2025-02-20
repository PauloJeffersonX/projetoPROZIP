import datetime

def calcular_idade():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        try:
            ano_nascimento = int(input("Digite o ano de seu nascimento (entre 1922 e 2021): "))
            
            if 1922 <= ano_nascimento <= 2021:
                break  # Sai do loop se o ano for válido
            else:
                print("Erro: O ano de nascimento deve estar entre 1922 e 2021.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido para o ano de nascimento.")

    ano_atual = 2022
    idade = ano_atual - ano_nascimento

    print("\nNome completo:", nome_completo)
    print("Idade em 2022:", idade, "anos")

calcular_idade()