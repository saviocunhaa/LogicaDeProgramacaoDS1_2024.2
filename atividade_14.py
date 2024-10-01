# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

# Recebe as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno foi aprovado, reprovado ou está de recuperação
if media >= 7:
    print(f"A média é {media:.2f}. O aluno foi aprovado.")
elif 5 <= media < 7:
    print(f"A média é {media:.2f}. O aluno está de recuperação.")
else:
    print(f"A média é {media:.2f}. O aluno foi reprovado.")
