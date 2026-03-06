# ==============================================================================
#        DESAFIO 037: CONVERSOR DE BASES NUMÉRICAS (MUNDO 2)
# ==============================================================================
from colorama import Fore, Style, init
init(autoreset=True)

# 1. ENTRADA DE DADOS
num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

# ------------------------------------------------------------------------------
# 2. LÓGICA DE CONVERSÃO (Utilizando ELIF)
# ------------------------------------------------------------------------------
# O Python já tem funções nativas: bin(), oct() e hex().
# Elas geram um prefixo (0b, 0o, 0x) que removemos com o fatiamento [2:].

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {Fore.YELLOW}{bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {Fore.YELLOW}{oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {Fore.YELLOW}{hex(num)[2:]}')
else:
    # O seu 'else' tinha uma condição. Lembre-se: else NÃO aceita condição!
    print(f'{Fore.RED}Opção inválida. Tente novamente.')

# ==============================================================================