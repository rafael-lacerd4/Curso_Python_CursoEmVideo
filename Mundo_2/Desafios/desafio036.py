"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
O programa  vai perguntar o 'valor da casa', o 'salário' do comprador e em 'quantos anos' ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou ent~]ao o empréstimo será negado.
"""
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Configurações de Estilo (Top do código)
SUCESSO = Fore.GREEN + Style.BRIGHT
ERRO = Fore.RED + Style.BRIGHT
ALERTA = Fore.YELLOW + Style.BRIGHT
TITULO = Back.BLUE + Fore.WHITE + Style.BRIGHT

print(f"{TITULO} {'SIMULADOR DE EMPRÉSTIMO BANCÁRIO':^40} {Style.RESET_ALL}")

# Entrada
valor_casa = float(input('Valor do imóvel: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? ')) # Usando int aqui

# Cálculos
meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

# Saída de dados formatada
print("-" * 40)
print(f"Para pagar um imóvel de R${valor_casa:,.2f} em {anos} anos,")
print(f"a prestação será de {Fore.CYAN}R${prestacao:.2f}{Fore.RESET} por mês.")
print(f"O limite de 30% do seu salário é R${limite:.2f}.")
print("-" * 40)

# Lógica Aninhada (Exemplo com ELIF para estudo)
if prestacao <= limite:
    print(f"Status: {SUCESSO}EMPRÉSTIMO APROVADO")
else:
    print(f"Status: {ERRO}EMPRÉSTIMO NEGADO")
    print(f"{Style.DIM}Motivo: Parcela excede o limite de segurança.")