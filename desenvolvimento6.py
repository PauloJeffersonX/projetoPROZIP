def calcular_idade():
    while True:
        nome = input("Digite seu nome completo: ")
        try:
            ano = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano <= 2021:
                idade = 2022 - ano
                print(f"\nNome: {nome}\nIdade em 2022: {idade} anos")
                return  # Sai da função após o sucesso
            else:
                print("Erro: Ano inválido.")
        except ValueError:
            print("Erro: Digite um número válido para o ano.")

calcular_idade()