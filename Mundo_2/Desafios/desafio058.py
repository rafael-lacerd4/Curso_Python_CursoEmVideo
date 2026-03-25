from random import randint
from time import sleep
from colorama import init, Fore

init(autoreset=True)

print(f'{Fore.CYAN}{" DESAFIO 058: ADIVINHAÇÃO 2.0 ":=^50}')

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    # --- BLOCO DE VALIDAÇÃO (O "ANTI-ERRO") ---
    while True:
        try:
            jogador = int(input('Qual seu palpite (0 a 10)? '))
            palpites += 1 # Cada entrada (certa ou errada) conta como palpite

            if 0 <= jogador <= 10:
                break # Sai deste while interno se o número for válido
            print(f"{Fore.RED}ERRO! O número deve estar entre 0 e 10.")
        except ValueError:
            print(f"{Fore.RED}ERRO! Digite apenas números inteiros.")
            # O contador de palpites já subiu ali em cima!

    # --- BLOCO DE COMPARAÇÃO ---
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print(f'Tente um número {Fore.YELLOW}MAIOR{Fore.RESET}...')
    else:
        print(f'Tente um número {Fore.YELLOW}MENOR{Fore.RESET}...')

print(f'\n{Fore.CYAN}PROCESSANDO...')
sleep(1)

print(f'🎉 {Fore.GREEN}PARABÉNS!{Fore.RESET} Eu realmente pensei no número {Fore.CYAN}{computador}.')
print(f'Você precisou de {Fore.YELLOW}{palpites}{Fore.RESET} palpites/tentativas para vencer.')
print(f'{Fore.CYAN}{"="*50}')