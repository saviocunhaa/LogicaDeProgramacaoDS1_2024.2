# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

total = 0
contador = 0

while True:
    numero = float(input("Digite um número -1 para sair: "))
    if numero == -1:
        break
    total += numero
    contador += 1

if contador == 0:
    print("Nenhum número foi inserido.")
else:
    media = total / contador
    print(f"A média dos números é: {media}")
