from random import randint

def numero_valido(x):
    if x.isnumeric():
        num_lados = int(x)
        if num_lados > 0:
            return True
    return False

def rolar_dados():
    while True:
        lados = input("Digite o número de lados do(s) dado(s): ")

        if lados == '':
            print('Programa finalizado')
            break

        if not numero_valido(lados):
            print('Número inválido!')
            continue

        num_lados = int(lados)

        num_rolagens = input('Quantos dados você deseja rolar? ')

        if num_rolagens == '':
            num_rolagens = 1
        elif not numero_valido(num_rolagens):
            print('Número inválido!')
            continue

        dados = int(num_rolagens)

        i = 0
        for dado in range(1, dados + 1):
            i += 1
            rolagem = randint(1, num_lados)
            print(f'Rolagem {i}: {rolagem}')

        print('')

rolar_dados()