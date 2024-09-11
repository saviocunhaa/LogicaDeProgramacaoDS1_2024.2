# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

#receber o valor do produto 
valorProduto = float(input("digite o valor do produto"))

#Calcular o valor do importo em relacao ao valor do produto
valorimposto = valorProduto * 12/100

#somar o valor do importo + valor do produto
valorFinal = valorProduto + valorimposto

print(f""" 
      O Valor do produto é: {valorProduto}
      O valor de imposto é: {valorimposto}
      O valor final com imposto é: {valorFinal}
""")

 