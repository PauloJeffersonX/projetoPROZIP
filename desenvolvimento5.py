def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        operacao = int(input("Digite a operação desejada: "))
        if operacao == 0:
            break  # Sai do loop   
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if operacao == 1:
            print("Resultado: ", num1 + num2)
        elif operacao == 2:
            print("Resultado: ", num1 - num2)
        elif operacao == 3:
            print("Resultado: ", num1 * num2)
        elif operacao == 4:
            if num2 == 0:  # Evita divisão por zero
                print("Não é possível dividir por zero")   
            else:
                print("Resultado: ", num1 / num2)
        else:
            print("Operação inválida")
calculadora()
