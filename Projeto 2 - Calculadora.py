calculadora = 0

while True:
    num1 = input('Informe o primeiro valor: ')
    
    if num1 == '':
        break
    numero1 = float(num1)

    print('''
    [+] Soma
    [-] Subtração
    [*] Multiplicação
    [/] Divisão
    ''')

    escolha = str(input('Digite o numero da operação que voce quer: '))

    if escolha == '':
        break

    print()

    num2 = input('Informe o segundo valor: ')

    if num2 == '':
        break

    numero2 = float(num2)

    if escolha == '+':
        calculadora = numero1 + numero2
        print(calculadora)
    elif escolha == '-':
        calculadora = numero1 - numero2
        print(calculadora)
    elif escolha == '*':
        calculadora = numero1 * numero2
        print(calculadora)
    elif escolha == '/':
        calculadora = numero1 / numero2
        print(calculadora)
    else:
        break
