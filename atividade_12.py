# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.

# Recebe a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verifica se a nota é maior ou igual a 7 para aprovação
if nota >= 7:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")
