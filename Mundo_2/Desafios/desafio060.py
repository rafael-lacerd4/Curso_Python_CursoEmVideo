"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

from colorama import init, Fore

init(autoreset=True)

print(f"{Fore.CYAN}{' Desafio 60 ':=^50}")


while True:
    try:
        n = int(input('Digite um número: '))
        if n == 0:
            print(f"{Fore.RED}ERRO! O número 0 não é permitido.")
        else:
            break
    except ValueError:
            print(f"{Fore.RED}ERRO! Digite apenas números inteiros.")


f = 1  # Essa é a nossa "caixa" (acumulador). Começa com 1.
print(f'Calculando {n}! = ', end='')

for c in range(n, 0, -1):
    print(f'{c}', end=' x ' if c > 1 else ' = ') # Esse é o seu print inteligente!
    f *= c  # Aqui a mágica acontece: f recebe ele mesmo vezes o contador atual.

print(f'{f}') # Mostra o resultado final que sobrou na caixa.