# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.

#recebero os valore em reais
real = float(input("digite sua quantidade e R$"))
dolar = float(input("digite o valor do cambio do dolar!"))

#conversao
valorConvertido = real / dolar

print(f" Seu valor em Dolar é: $ {valorConvertido}")

