
print("--- Padaria YYZ ---")
paes = int(input("Quantidade de pães vendidos: "))
broas = int(input("Quantidade de broas vendidas: "))


valor_paes = paes * 0.12
valor_broas = broas * 1.50
total_vendas = valor_paes + valor_broas
reserva_poupanca = total_vendas * 0.10

print("-" * 20)
print(f"Total arrecadado: R$ {total_vendas:.2f}")
print(f"Valor para poupança: R$ {reserva_poupanca:.2f}")
