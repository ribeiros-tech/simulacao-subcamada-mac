import random
import time

# ==============================
# SIMULAÇÃO DO PROTOCOLO TOKEN RING
# ==============================

stations = ["A", "B", "C", "D", "E"]
token_position = 0
rounds = 10

print("\n=== SIMULAÇÃO DO PROTOCOLO TOKEN RING ===\n")

for round_number in range(1, rounds + 1):
    print(f"🔄 Rodada {round_number}")

    current_station = stations[token_position]
    print(f"🎫 Token com a estação {current_station}")

    # Decide se a estação tem dados para transmitir
    has_data = random.choice([True, False])

    if has_data:
        print(f"📤 Estação {current_station} transmitiu seus dados")
    else:
        print(f"📭 Estação {current_station} não tem dados para transmitir")

    print("➡️ Token passado para a próxima estação\n")

    token_position = (token_position + 1) % len(stations)
    time.sleep(1)

print("=== RESULTADO FINAL (TOKEN RING) ===")
print("Nenhuma colisão ocorreu durante a simulação.")
