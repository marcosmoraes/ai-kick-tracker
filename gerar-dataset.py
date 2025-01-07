import json
import random

# Função para gerar um dataset simulado
def gerar_cobrancas(qtd=1000):
    cobrancas = []
    for i in range(1, qtd + 1):
        cobranca = {
            "cobranca": i,
            "distancia": round(random.uniform(10, 30), 1),  # Distância em metros
            "angulo": round(random.uniform(20, 60), 1),    # Ângulo em graus
            "altura": round(random.uniform(0.5, 3.0), 1),  # Altura em metros
            "velocidade": round(random.uniform(10, 40), 1), # Velocidade em m/s
            "resultado": random.choice([0, 1])             # Resultado (0 ou 1)
        }
        cobrancas.append(cobranca)
    return cobrancas

# Gerar 1000 cobranças simuladas
dataset = gerar_cobrancas(1000)

# Salvar em um arquivo JSON
with open("cobrancas_simuladas_1000.json", "w") as file:
    json.dump(dataset, file, indent=4)

print("Dataset gerado com sucesso!")
