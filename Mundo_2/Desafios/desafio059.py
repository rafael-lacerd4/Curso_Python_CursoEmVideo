"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from colorama import init, Fore
from time import sleep

init(autoreset=True)

print(f'{Fore.CYAN}{" DESAFIO 059: MENU ":=^50}')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0  # <--- IMPORTANTE: Definir antes de começar o while!

while opcao != 5:
    print(f'{Fore.CYAN}=-=' * 10)
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    try:
        opcao = int(input('>>>> Qual é a sua opção? '))
    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número de 1 a 5.')
        continue

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {Fore.GREEN}{soma}')

    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {Fore.GREEN}{produto}')

    elif opcao == 3:
        # --- SEU DESAFIO ESTÁ AQUI ---
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {Fore.GREEN}{n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior é {Fore.GREEN}{n2}')
        else:
            print(f'{Fore.YELLOW}Os dois valores são IGUAIS.')

    elif opcao == 4:
        print(f'{Fore.MAGENTA}Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print(f'{Fore.RED}Finalizando...')

    else:
        print(f'{Fore.RED}Opção inválida. Tente novamente.')

    print(f'{Fore.CYAN}=-=' * 10)
    sleep(1.5)  # Dá tempo do usuário ler o resultado antes do menu subir

print(f'\n{Fore.GREEN}Fim do programa! Volte sempre.')