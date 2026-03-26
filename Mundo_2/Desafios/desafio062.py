"""
Melhore o DESAFIO 061
"""
from colorama import Fore, init
from time import sleep  # Importante para o efeito de tempo

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 062: PA SUPER TURBO ':=^50}")

# Validação inicial dos dados
while True:
    try:
        primeiro = int(input("Primeiro termo: "))
        razao = int(input("Razão da PA: "))
        break
    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f' {Fore.YELLOW}{termo} {Fore.RESET}→', end='', flush=True)
        sleep(0.3)  # <--- O efeito de carregamento aqui!
        termo += razao
        cont += 1

    print(f' {Fore.MAGENTA}PAUSA')

    # --- NOVA VALIDAÇÃO PARA OS TERMOS EXTRAS ---
    while True:
        try:
            mais = int(input('\nQuantos termos você quer mostrar a mais? (0 para sair): '))
            break  # Sai desta validação se for um número
        except ValueError:
            print(f'{Fore.RED}ERRO! Digite um número inteiro (ex: 5, 10, 0).')
    # --------------------------------------------

print(f'\n{Fore.CYAN}{"=" * 50}')
print(f'Progressão finalizada com {Fore.GREEN}{total}{Fore.RESET} termos mostrados.')