"""
A confederação nacional de ntação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: mirim
#Até 14 anos: ifantil
#Até 19 anos: Junior
#Até 20 anos: Senior
acima: master
"""
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

print(f"{Fore.CYAN}{' DESAFIO 41 ':=^50}")

# 1. ENTRADA E VALIDAÇÃO
while True:
    try:
        ano_atual = datetime.now().year
        nasc = int(input('Ano de Nascimento: '))

        # Validação para não aceitar anos absurdos (Futuro ou muito antigo)
        if 1900 <= nasc <= ano_atual:
            break  # Agora sim o break sai do loop quando o dado é válido
        else:
            print(f"{Fore.RED}ERRO! Digite um ano entre 1900 e {ano_atual}.")
    except ValueError:
        print(f"{Fore.RED}ENTRADA INVÁLIDA: Por favor, digite apenas números (4 dígitos).")

# 2. CÁLCULO DA IDADE (Corrigido: Atual - Nascimento)
idade = ano_atual - nasc

print(f"\nO atleta tem {Fore.YELLOW}{idade}{Fore.RESET} anos.")

# ------------------------------------------------------------------------------
# 3. LÓGICA DE CATEGORIAS (Escadinha de ELIF)
# ------------------------------------------------------------------------------
# A vantagem do ELIF é que não precisamos testar "se é maior que 9 e menor que 14"
# Se o Python passou pelo primeiro IF, ele JÁ SABE que o atleta tem mais de 9 anos.

if idade <= 9:
    print(f'Classificação: {Fore.GREEN}MIRIM')
elif idade <= 14:
    print(f'Classificação: {Fore.GREEN}INFANTIL')
elif idade <= 19:
    print(f'Classificação: {Fore.GREEN}JUNIOR')
elif idade <= 25:  # Ajustado para o padrão comum (25 anos), mas você pode mudar para 20
    print(f'Classificação: {Fore.GREEN}SÊNIOR')
else:
    print(f'Classificação: {Fore.GREEN}MASTER')

print(f"{Fore.CYAN}{'=' * 50}")