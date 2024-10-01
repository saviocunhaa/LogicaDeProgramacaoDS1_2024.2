# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

# Recebe o peso e a altura da pessoa
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Exibe o valor do IMC
print(f"O IMC é: {imc:.2f}")

# Classifica o IMC de acordo com a tabela
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal.")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso.")
else:
    print("Classificação: Obesidade.")
