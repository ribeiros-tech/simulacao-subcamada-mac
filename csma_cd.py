import random
import time

# ==============================
# SIMULAÇÃO DO PROTOCOLO CSMA/CD
# ==============================

stations = ["A", "B", "C", "D", "E"]
total_time_slots = 10

print("\n=== SIMULAÇÃO DO PROTOCOLO CSMA/CD ===\n")

successful_transmissions = 0
collisions = 0

for time_slot in range(1, total_time_slots + 1):
    print(f"⏱️ Tempo {time_slot}")

    # Estação candidata a transmitir
    station = random.choice(stations)

    # Verifica se o canal está livre
    channel_free = random.choice([True, True, False])

    if channel_free:
        print(f"Estação {station} detectou o canal LIVRE e iniciou transmissão")

        # Durante a transmissão pode ocorrer colisão
        collision_detected = random.choice([False, False, True])

        if collision_detected:
            print("❌ Colisão detectada DURANTE a transmissão")
            print("⛔ Transmissão interrompida imediatamente\n")
            collisions += 1
        else:
            print("✅ Transmissão concluída com sucesso\n")
            successful_transmissions += 1
    else:
        print(f"Estação {station} detectou o canal OCUPADO")
        print("⏳ Aguardando novo tempo para transmitir\n")

    time.sleep(1)

print("=== RESULTADO FINAL (CSMA/CD) ===")
print(f"Transmissões bem-sucedidas: {successful_transmissions}")
print(f"Colisões detectadas: {collisions}")
