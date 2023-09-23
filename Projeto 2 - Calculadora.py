calculadora = 0

while True:
    print('''
    Calculadora
    ===============================
    [+] Soma
    [-] Subtração
    [*] Multiplicação
    [/] Divisão
    ===============================
    [x] Limpar calculadora
    [ENTER] Encerra o programa
    ===============================
    ''')

    escolha = input('Digite o sinal da operação que você quer usar: ').lower()

    if escolha == '':
        break

    if escolha == 'x':
        calculadora = 0
        continue

    if calculadora == 0:
        num1 = input('Informe o primeiro valor: ')

        if num1 == '':
            print('Processo finalizado.')
            break

        numero1 = float(num1)

    else:
        numero1 = calculadora

    num2 = input('Informe o segundo valor: ')

    if num2 == '':
        print('Processo finalizado.')
        break

    numero2 = float(num2)

    if escolha == '+':
        calculadora = numero1 + numero2
        print(f'O resultado foi: {calculadora}')
    elif escolha == '-':
        calculadora = numero1 - numero2
        print(f'O resultado foi: {calculadora}')
    elif escolha == '*':
        calculadora = numero1 * numero2
        print(f'O resultado foi: {calculadora}')
    elif escolha == '/':
        if numero2 == 0:
            print('Não é possível dividir por zero.')
        else:
            calculadora = numero1 / numero2
            print(f'O resultado foi: {calculadora}')
    else:
        print('Algo foi digitado de forma errada. Digite novamente!')
