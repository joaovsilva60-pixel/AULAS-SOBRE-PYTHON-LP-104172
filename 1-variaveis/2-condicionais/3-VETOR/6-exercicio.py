import os
os.system("cls")

print('=== INSERINDO NOTAS NO VETOR ===')

vetor_notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    vetor_notas.append(nota)

# Calculando a média aritmética
media = sum(vetor_notas) / QUANTIDADE_NOTAS

print('\n=== EXIBINDO AS NOTAS DO VETOR ===')

for posicao, nota in enumerate(vetor_notas, start=1):
    print(f'{posicao}ª nota: {nota}')

print(f'\nMédia: {media:.2f}')

# Verificando a situação do aluno
if media >= 7:
    print('Situação: Aprovado')
elif media >= 5:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')
