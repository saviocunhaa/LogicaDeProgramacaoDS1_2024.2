# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

# Recebe um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
