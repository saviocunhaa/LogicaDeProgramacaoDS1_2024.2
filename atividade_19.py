# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

#resolucao com For
numero = int(input("digite um valor"))
i = 2
result = 1
for i in range(1, numero + 1):
    result = result * i
   
print(result)

#resolucao com While

numero2 = int(input("digite um valor"))
resultado2 = 1
j = 2
while j <= numero2:
    resultado2 = resultado2 * j
    j = j + 1 

print(resultado2)