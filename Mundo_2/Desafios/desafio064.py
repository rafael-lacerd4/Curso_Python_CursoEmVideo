"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999 (que é a condição de parada/flag). No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
from colorama import init, Fore

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 064: TRATANDO VALORES ':=^50}")

soma = cont = 0

while True:
    try:
        n = int(input("Digite um número [999 para parar]: "))

        # 1. O "Porteiro" (Verifica se deve parar)
        if n == 999:
            break  # Sai do loop imediatamente e ignora o que está abaixo

        # 2. A "Contabilidade" (Deve estar FORA do IF acima)
        # Repare que estas linhas estão na mesma coluna do 'if'
        soma += n
        cont += 1

    except ValueError:
        print(f'{Fore.RED}ERRO! Digite um número inteiro válido.')

# Aqui o programa chega depois do break
print(f"{Fore.GREEN}{'=' * 50}")
print(f"Você digitou {Fore.YELLOW}{cont}{Fore.RESET} números.")
print(f"A soma entre eles foi {Fore.YELLOW}{soma}{Fore.RESET}.")