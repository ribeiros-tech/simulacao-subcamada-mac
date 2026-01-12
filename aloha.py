import random
import time

# ==============================
# SIMULAÇÃO DO PROTOCOLO ALOHA
# ==============================

# Lista de estações da rede
stations = ["A", "B", "C", "D", "E"]

# Parâmetros da simulação
total_time_slots = 10
max_transmissions = 3

print("\n=== SIMULAÇÃO DO PROTOCOLO ALOHA ===\n")

successful_transmissions = 0
collisions = 0

for time_slot in range(1, total_time_slots + 1):
    print(f"⏱️ Tempo {time_slot}")

    # Sorteia quantas estações vão tentar transmitir
    num_transmitting = random.randint(1, max_transmissions)

    # Escolhe as estações aleatoriamente
    transmitting_stations = random.sample(stations, num_transmitting)

    print(f"Estações transmitindo: {transmitting_stations}")

    # Verifica colisão
    if len(transmitting_stations) == 1:
        print("✅ Transmissão realizada com sucesso\n")
        successful_transmissions += 1
    else:
        print("❌ Colisão detectada!")
        print("As estações irão aguardar tempo aleatório para retransmitir\n")
        collisions += 1

    time.sleep(1)

# Resultados finais
print("=== RESULTADO FINAL (ALOHA) ===")
print(f"Transmissões bem-sucedidas: {successful_transmissions}")
print(f"Colisões ocorridas: {collisions}")
