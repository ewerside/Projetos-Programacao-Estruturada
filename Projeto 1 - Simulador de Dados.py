from random import randint

def numero_valido(x):
    if x.isnumeric():
        num_lados = int(x)
        if num_lados > 0:
            return True
    return False

def rolar_dados():
    while True:
        lados = input("Digite o número de lados do(s) dado(s). (Ou pressione ENTER para sair.) ")

        if lados == '':
            print('Programa finalizado')
            break

        if not numero_valido(lados):
            print('Por favor, digite um número maior que zero.')
            continue

        num_lados = int(lados)

        while True:
            dados = input('Quantos dados você deseja rolar? (Pressione ENTER para rolar apenas 1.) ')

            if dados == '':
                dados = 1
            elif not numero_valido(dados):
                print('Por favor, digite um número maior que zero.')
                continue
            break

        num_rolagens = int(dados)

        valores_rolados = []

        i = 0
        for dado in range(1, num_rolagens + 1):
            i += 1
            rolagem = randint(1, num_lados)
            print(f'Rolagem {i}: {rolagem}')
            valores_rolados.append(rolagem)

        print(f'{num_rolagens} dado(s) de {num_lados} lado(s): {valores_rolados}\n')

rolar_dados()