# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
idade = int(input("digite sua idade ")) 
# Criança (0-12 anos)
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
# Adulto (18-59 anos)
elif idade <= 59:
    print("Adulto")
# Idoso (60 anos ou mais)
else:
    print("Idoso")

