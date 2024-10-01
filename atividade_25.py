# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
aprovados = 0

for i in range(1, 6):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    if nota >= 7:
        aprovados += 1

print(f"Quantidade de alunos aprovados: {aprovados}")


