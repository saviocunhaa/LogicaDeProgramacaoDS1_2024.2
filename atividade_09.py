# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

#receber a quantidade de km percorrido

#receber a quantidade de 
# Recebe a quantidade de quilômetros percorridos
km_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))

# Recebe a quantidade de litros de combustível consumidos
litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))

# Calcula o consumo médio (km por litro)
consumo_medio = km_percorridos / litros_consumidos

# Exibe o resultado
print(f"O consumo médio de combustível é de {consumo_medio:.2f} km/l.")
