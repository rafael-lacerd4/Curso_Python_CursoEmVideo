# ==========================================================
# ESTRUTURA DE REPETIÇÃO WHILE (AULA 14)
# ==========================================================

# 1. COMPARANDO FOR E WHILE (Quando sabemos o limite)
# Ambos fazem a mesma coisa aqui: contam de 1 a 9.
for c in range(1, 10):
    print(c)
print('Fim do For')

c = 1
while c < 10:
    print(c)
    c += 1  # Importante: se não somar, o laço é infinito!
print('Fim do While')

# ----------------------------------------------------------
# 2. O "FLAG" (Ponto de Parada)
# Quando não sabemos quantas vezes o usuário vai digitar.
n = 1
while n != 0:  # Enquanto n for diferente de 0, o jogo continua
    n = int(input('Digite um valor [0 para parar]: '))
print('Fim do Flag')

# ----------------------------------------------------------
# 3. VALIDAÇÃO DE CONTINUIDADE
# Note o ajuste: R = 'S' e while R == 'S' (Python diferencia maiúsculas)
R = 'S'
while R == 'S':
    n = int(input('Digite um valor: '))
    # O .upper() garante que mesmo que digite 's' minúsculo, vire 'S'
    R = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Fim da Validação')

# ----------------------------------------------------------
# 4. ANALISADOR DE NÚMEROS (Pares e Ímpares)
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:  # Check para não contar o '0' da parada como par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} números pares e {impar} números ímpares!')


