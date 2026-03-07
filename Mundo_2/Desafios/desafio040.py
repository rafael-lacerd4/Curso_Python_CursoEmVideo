"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a meia atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: Recuperação
#Media 7.0 ou superior: Aprovado
"""
# ==============================================================================
#           DESAFIO 040: MÉDIA DO ALUNO (COM CORES E VALIDAÇÃO)
# ==============================================================================
# ==============================================================================
#           DESAFIO 040: MÉDIA DO ALUNO (BLINDADO COM TRY/EXCEPT)
# ==============================================================================
from colorama import Fore, Style, init

init(autoreset=True)

print(f"{Fore.MAGENTA}{' CONTROLE DE NOTAS ':-^50}{Fore.RESET}")

# 1. LOOP DE VALIDAÇÃO COMPLETA
while True:
    try:
        # Tenta converter a entrada para float
        n1 = float(input('Digite a primeira nota (0-10): '))
        n2 = float(input('Digite a segunda nota (0-10): '))

        # Se chegou aqui, são números. Agora testamos se estão entre 0 e 10.
        if 0 <= n1 <= 10 and 0 <= n2 <= 10:
            break  # Sucesso total! Sai do loop.
        else:
            print(f"{Fore.RED}ERRO: As notas precisam ser entre 0.0 e 10.0.")

    except ValueError:
        # Se o usuário digitar letras ou símbolos, o 'try' pula para cá
        print(f"{Fore.RED}ENTRADA INVÁLIDA: Por favor, digite apenas números.")

# 2. CÁLCULO DA MÉDIA
media = (n1 + n2) / 2

print(f"\nNotas: {n1} e {n2} | Média Final: {Fore.CYAN}{media:.1f}")

# 3. LÓGICA DE CLASSIFICAÇÃO
if media < 5.0:
    print(f"Resultado: {Fore.RED}{Style.BRIGHT}REPROVADO")
elif 5.0 <= media <= 6.9:
    print(f"Resultado: {Fore.YELLOW}{Style.BRIGHT}RECUPERAÇÃO")
else:
    print(f"Resultado: {Fore.GREEN}{Style.BRIGHT}APROVADO")

print(f"{Fore.MAGENTA}{'=' * 50}")