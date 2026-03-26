"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
from colorama import Fore, init

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 061: PROGRESSÃO ARITMÉTICA ':=^50}")

while True:
    try:
        primeiro = int(input("Primeiro termo: "))
        razao = int(input("Razão da PA: "))
        break
    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

print(f"\nOs 10 primeiros termos dessa PA são:")
print(f"{Fore.YELLOW}=", end="")


termo = primeiro
cont = 1

while cont <= 10:
    print(f' {termo} → ', end='')

    # O SEGREDO ESTÁ AQUI:
    termo += razao  # O termo "pula" para o próximo valor
    cont += 1  # O contador avisa que um termo já foi mostrado

print('FIM')