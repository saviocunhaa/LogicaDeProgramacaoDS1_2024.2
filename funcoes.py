def valor_imposto(valor):
    if valor <= 1000:
        imposto = valor * 0.1
    elif valor <= 2000: 
        imposto = valor * 0.13
    else:
        imposto = valor * 0.20
    return imposto

produto1 = float(input("digite o valor do produto 1"))
produto2 = float(input("digite o valor do produto 2"))
produto3 = float(input("digite o valor do produto 3"))
produto4 = float(input("digite o valor do produto 4"))


valor_atual_com_imposto = valor_imposto(produto1)
valor_atual_com_imposto2 = valor_imposto(produto2)
valor_atual_com_imposto3 = valor_imposto(produto3)
valor_atual_com_imposto4 = valor_imposto(produto4)

print(f"""
      o imposto do produto e 1 - {valor_atual_com_imposto}
      o imposto do produto e 2 - {valor_atual_com_imposto2}
      o imposto do produto e 3 - {valor_atual_com_imposto3}
      o imposto do produto e 4 - {valor_atual_com_imposto4}
      """)
