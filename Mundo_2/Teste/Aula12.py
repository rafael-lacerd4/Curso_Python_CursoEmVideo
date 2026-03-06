# ==============================================================================
#           ESTRUTURA CONDICIONAL ANINHADA (IF... ELIF... ELSE)
# ==============================================================================

# O método .title() garante que a primeira letra seja sempre Maiúscula.
nome = str(input('Qual é seu nome? ')).strip().title()

# --- A ESTRUTURA ANINHADA ---
# Imagine isso como um funil de decisões:

if nome == 'Rafael':
    # Se a primeira condição for VERDADEIRA, o Python executa aqui e ignora o resto.
    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    # O 'elif' (else if) só é testado se o 'if' lá de cima for FALSO.
    # Aqui usamos o operador lógico 'or' para testar várias opções.
    print('Seu nome é bem popular no Brasil.')

elif nome in 'Ana Cláudia Jéssica Juliana':
    # O operador 'in' verifica se o que o usuário digitou está DENTRO da string.
    # Ex: Se digitar "Ana", ele encontra "Ana" dentro de "Ana Cláudia...".
    print('Belo nome feminino!')

else:
    # O 'else' é o "porto seguro". Se nenhuma das opções acima serviu, ele entra aqui.
    print('Seu nome é bem normal.')

# Esta linha está fora de todos os blocos (sem espaço no começo). 
# Por isso, ela sempre será executada, independente do nome.
print(f'Tenha um bom dia, {nome}!')

# ==============================================================================