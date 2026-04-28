# Entrada de dados
nome_carro = input("Nome do automóvel: ")
preco_fabrica = float(input("Preço de fábrica: R$ "))

# Cálculos
valor_impostos = preco_fabrica * 0.35
lucro_revendedor = preco_fabrica * 0.15
preco_final = preco_fabrica + valor_impostos + lucro_revendedor

# Saída
print("-" * 30)
print(f"Automóvel: {nome_carro}")
print(f"Preço de fábrica: R$ {preco_fabrica:.2f}")
print(f"Valor dos impostos (35%): R$ {valor_impostos:.2f}")
print(f"Lucro do revendedor (15%): R$ {lucro_revendedor:.2f}")
print(f"Preço final ao consumidor: R$ {preco_final:.2f}")
