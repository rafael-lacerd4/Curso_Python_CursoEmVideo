from colorama import init, Fore

init(autoreset=True)

resp = 'S'
soma = quant = maior = menor = 0

while resp in 'Ss':
    try:
        n = int(input('Digite um número: '))
        soma += n
        quant += 1

        if quant == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        resp = ' '  # Começa vazio para entrar no loop abaixo
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if resp not in 'SN':
                print(f'{Fore.RED}OPÇÃO INVÁLIDA! Digite apenas S ou N.')
    except (ValueError, IndexError):
        print(f'{Fore.RED}Entrada inválida! Digite um número inteiro.')
# Fora do While: Cálculos Finais
if quant > 0:
    media = soma / quant
    print(f'\n{Fore.CYAN}{"=" * 40}')
    print(f'Você digitou {quant} números e a média foi {media:.2f}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print('Nenhum número foi digitado.')