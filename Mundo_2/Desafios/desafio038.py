"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.
"""
from colorama import Fore, init
init(autoreset=True)

print(f"{'Desafio 38':=^50}")

#entrada

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#condição e logica
if n1 > n2:
    print(f'O primeiro valor {Fore.BLUE}{n1}{Fore.RESET} é maior.')
elif n2 > n1:
    print(f'O segundo valor {Fore.YELLOW}{n2}{Fore.RESET} é maior.')
else:
    print(f'Não existe valor maior, o numero {Fore.BLUE}{n1}{Fore.RESET} é igual ao numero {Fore.YELLOW}{n2}{Fore.RESET}')