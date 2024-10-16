# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

VALOR_PI = 3.13

def calcular_area_base(raio):
    VALOR_PI = 3.14
    print(VALOR_PI)
    area = VALOR_PI * raio ** 2
    return area

def calcular_volume_cilindro(raio, altura):
    print(VALOR_PI)
    valor_area = calcular_area_base(raio)
    volume = valor_area * altura
    return volume

raio_informado = int(input('digite o valor do raio'))
altura_informado = int(input('digite a altura'))

resultado = calcular_volume_cilindro(raio_informado, altura_informado)

print(resultado)



