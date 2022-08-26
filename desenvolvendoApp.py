acumulador = 0
print("Seja Bem -Vindo a Pizzaria do Alex Inácio Pereira")
while True:
    print("**********Opções de Serviço**********")
    print("| Código | Descrição  | Pizza Média | Pizza Grange |")
    print("|   21   | Napolitana |   R$ 20,00  |      R$26,00 |")
    print("|   22   | Margherita |   R$ 20,00  |      R$26,00 |")
    print("|   23   | Calabresa  |   R$ 25,00  |      R$32,50 |")
    print("|   24   | Toscana    |   R$ 30,00  |      R$39,00 |")
    print("|   25   | Portuguesa |   R$ 30,00  |      R$39,00 |")
    tamanho = input("Qual o tamanho da Pizza que você deseja (M / G): ")
    if tamanho == "M":
        sabor = int(input("entre com o código desejado:"))
        if sabor == 21:
            acumulador = acumulador + 20
            print("Você escolheu o Sabor Napolitana")
        elif sabor == 22:
            acumulador = acumulador + 20
            print("Você escolhey o Sabor margherita")
        elif sabor == 23:
            acumulador = acumulador + 25
            print("Você escolhey o Sabor Calabresa")
        elif sabor == 24:
            acumulador = acumulador + 30
            print("Você escolhey o Sabor Toscana")
        elif sabor == 25:
            acumulador = acumulador + 30
            print("Você escolhey o Sabor Portuguesa")
        else:
            print("Opção Inválida")
            continue

    elif tamanho == "G":
        sabor = int(input("entre com o código desejado:"))
        if sabor == 21:
            print("você escolheu o Sabor Napolitana")
            acumulador = acumulador + 26
        elif sabor == 22:
            print("Você escolheu o sabor Margherita")
            acumulador = acumulador + 26
        elif sabor == 23:
            print("Você escolheu o sabor Calabresa")
            acumulador = acumulador + 32.50
        elif sabor == 24:
            print("Você escolheu o sabor Toscana")
            acumulador = acumulador + 39
        elif sabor == 25:
            print("Você escolheu o sabor Portuguesa")
            acumulador = acumulador + 39
    else:
        print("Opção inválida")
        continue
    resposta = input("Deseja Continuar: \n 1 - Sim \n 2- Não")
    if resposta == "1":
        continue
    else:
        print("O valor final da conta é:{:.2f}".format(acumulador))


