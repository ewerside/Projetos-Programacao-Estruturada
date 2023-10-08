def calculadora():
    calculo = 0
    estado_inicial = True

    while True:
        print(calculo)
        if estado_inicial:
            primeiro_valor = input('Informe o primeiro valor ou aperte ENTER para sair: ')

            if primeiro_valor == '':
                print('Processo finalizado.')
                break

            primeiro_numero = float(primeiro_valor)
            estado_inicial = False
        else:
            primeiro_numero = calculo

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

        segundo_valor = input('Informe o segundo valor ou aperte ENTER para sair: ')

        if segundo_valor == '':
            print('Processo finalizado.')
            break

        segundo_numero = float(segundo_valor)

        if operacao == '+':
            calculo = primeiro_numero + segundo_numero
        elif operacao == '-':
            calculo = primeiro_numero - segundo_numero
        elif operacao == '*':
            calculo = primeiro_numero * segundo_numero
        else:
            # O else acaba tratando da operação de divisão. Como o problema pede
            # para considerar que os valores digitados sempre serão válidos, também
            # não tratamos da divisão por zero.
            calculo = primeiro_numero / segundo_numero

calculadora()