"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' OU 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor coreto
"""
from colorama import init, Fore
init(autoreset=True)

print(f'{Fore.CYAN}{" Desafio 57 ":=^50}')

while True:
    sexo = input('QUAL É SEU SEXO? DIGITE [M/F]:').strip().upper()
    if sexo in ('M', 'F'): break
    print(f"{Fore.RED}Digite M ou F.")
print(f'Seu sexo é {Fore.GREEN}{sexo}')
