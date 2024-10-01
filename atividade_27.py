    # Você está organizando um churrasco e precisa gerenciar a lista de convidados. Crie um programa em Python que:

    # Solicite ao usuário que insira o nome de até 7 convidados.
    # Armazene os nomes em uma lista.
    # Permita ao usuário remover um convidado da lista, caso necessário.
    # Exiba a lista final de convidados.

    # Digite o nome do convidado 1: João
    # Digite o nome do convidado 2: Maria
    # ...
    # Digite o nome do convidado 7: Pedro
    # Deseja remover algum convidado da lista? (sim/não): sim
    # Digite o nome do convidado a ser removido: Maria

# Lista para armazenar os nomes dos convidados
listaChurras = []

# Solicitar o nome de até 7 convidados
for i in range(1, 8):
    nome = input(f"Digite o nome do convidado {i}: ")
    listaChurras.append(nome)

# Exibir a lista de convidados
print("\nLista de convidados:")
for convidado in listaChurras:
    print(convidado)

# Perguntar se o usuário deseja remover algum convidado
remover = input("\nDeseja remover algum convidado da lista? (sim/não): ").lower()
# lower(): Converte a string inserida pelo usuário para letras minúsculas.


if remover == "sim":
    nome_remover = input("Digite o nome do convidado a ser removido: ")
    if nome_remover in listaChurras:
        listaChurras.remove(nome_remover)
        print(f"\nConvidado {nome_remover} removido com sucesso!")
    else:
        print(f"\nConvidado {nome_remover} não está na lista.")

# Exibir a lista final de convidados
print("\nLista final de convidados:")
for convidado in listaChurras:
    print(convidado)
