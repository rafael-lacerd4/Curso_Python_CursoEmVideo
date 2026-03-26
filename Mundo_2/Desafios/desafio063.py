"""
Desafio 063 (Sequência de Fibonacci)
"""
from colorama import init, Fore

init(autoreset=True)

print (F"{Fore.CYAN}{" Trabalho de Fibonacci ":=^50}")

while True:
    try:
        n =int( input(" Digite Quantos termos você deseja: "))
        break
    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

t1 = 0
t2 = 1

print(f'{Fore.YELLOW}{t1} → {t2}', end='')  # Mostramos os dois primeiros fora do laço

cont = 3  # Começamos o contador no 3, pois já mostramos dois termos
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')

    # A MÁGICA DA TROCA:
    t1 = t2
    t2 = t3

    cont += 1  # Não esqueça de subir o contador!

print(f' → {Fore.CYAN}FIM')