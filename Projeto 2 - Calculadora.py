calculo = 0
estado_inicial = True

while True:
    print(calculo)
    if estado_inicial:
        num1 = input('Informe o primeiro valor ou aperte ENTER para sair: ')

        if num1 == '':
            print('Processo finalizado.')
            break

        numero1 = float(num1)
        estado_inicial = False
    else:
        numero1 = calculo

    operacao = input("Digite a operação desejada:\n"
                     "===============================\n"
                     "[+] Soma\n"
                     "[-] Subtração\n"
                     "[*] Multiplicação\n"
                     "[/] Divisão\n"
                     "===============================\n"
                     "[ENTER] Encerra o programa\n"
                     "[*] Multiplicação\n"
                     "===============================\n").lower()

    if operacao == '':
        print('Processo finalizado.')
        break

    if operacao == 'x':
        calculo = 0
        estado_inicial = True
        continue

    num2 = input('Informe o segundo valor ou aperte ENTER para sair: ')

    if num2 == '':
        print('Processo finalizado.')
        break

    numero2 = float(num2)

    if operacao == '+':
        calculo = numero1 + numero2
    elif operacao == '-':
        calculo = numero1 - numero2
    elif operacao == '*':
        calculo = numero1 * numero2
    else:
        # O else acaba tratando da operação de divisão. Como o problema pede
        # para considerar que os valores digitados sempre são válidos, também
        # não tratamos da divisão por zero.
        calculo = numero1 / numero2