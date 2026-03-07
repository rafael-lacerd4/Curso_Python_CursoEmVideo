"""
Faça um programa que leia o ano de nascimento de uma jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar.
# Se já passou do tempo do alistamento

Seu programa também deverá mostar o tempo que faltou ou passou do prazo
"""
# ==============================================================================
#        DESAFIO 039: ALISTAMENTO MILITAR COM VALIDAÇÃO DE SEXO
# ==============================================================================
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)
print(f"{' DESAFIO 039 ':=^50}")

# 1. ENTRADA DE DADOS
ano_atual = datetime.now().year
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

# 2. VALIDAÇÃO INICIAL (O alistamento só segue se for Masculino)
if sexo == 'F':
    print(f"\n{Fore.CYAN}No Brasil, o alistamento militar não é obrigatório para mulheres.")
    print("Tenha um bom dia!")

elif sexo == 'M':
    nasc = int(input('Ano de Nascimento (ex: 1998): '))
    idade = ano_atual - nasc
    print(f"\nQuem nasceu em {nasc} tem {Fore.CYAN}{idade} anos{Fore.RESET} em {ano_atual}.")

    # 3. LÓGICA DE IDADE (Aninhada dentro do sexo Masculino)
    if idade == 18:
        print(f"{Fore.YELLOW}Você tem que se alistar IMEDIATAMENTE!")

    elif idade < 18:
        saldo = 18 - idade
        ano = ano_atual + saldo
        print(f"Ainda faltam {Fore.GREEN}{saldo} ano(s){Fore.RESET} para o alistamento.")
        print(f"Seu alistamento será em {Fore.GREEN}{ano}{Fore.RESET}.")

    else:
        saldo = idade - 18
        ano = ano_atual - saldo
        print(f"Você já deveria ter se alistado há {Fore.RED}{saldo} ano(s){Fore.RESET}.")
        print(f"Seu alistamento foi em {Fore.RED}{ano}{Fore.RESET}.")

else:
    print(f"{Fore.RED}Opção de sexo inválida. Por favor, use M ou F.")

# ==============================================================================
