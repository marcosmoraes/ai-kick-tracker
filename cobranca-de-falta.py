import json
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# Carregar o JSON
try:
    with open("../ai-linear-regression/cobrancas_simuladas_1000.json", "r") as file:
        dataset = json.load(file)
except FileNotFoundError:
    print("Erro: O arquivo 'cobrancas_simuladas.json' não foi encontrado.")
    exit()
except json.JSONDecodeError:
    print("Erro: O arquivo 'cobrancas_simuladas.json' não contém um JSON válido.")
    exit()

# Converter JSON para DataFrame
df = pd.DataFrame(dataset)

# Validar a presença das colunas necessárias
required_columns = ["cobranca", "resultado", "distancia", "angulo", "altura", "velocidade"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f"Erro: As seguintes colunas estão ausentes no JSON: {', '.join(missing_columns)}")
    exit()

# Calcular a taxa de sucesso acumulada
df = df.sort_values(by="cobranca")  # Ordenar pelo número da cobrança
df["sucesso_acumulado"] = df["resultado"].expanding().mean() * 100  # Taxa acumulada em %

# Identificar intervalos ideais para cada variável com base nos dados de sucesso
success_data = df[df["resultado"] == 1]
distancia_range = (success_data["distancia"].min(), success_data["distancia"].max())
angulo_range = (success_data["angulo"].min(), success_data["angulo"].max())
altura_range = (success_data["altura"].min(), success_data["altura"].max())
velocidade_range = (success_data["velocidade"].min(), success_data["velocidade"].max())

# Criar gráfico de evolução da performance
plt.figure(figsize=(12, 10))  # Ajustar o tamanho do gráfico
plt.plot(df["cobranca"], df["sucesso_acumulado"], color="blue", label="Taxa de Sucesso Acumulada")

# Adicionar linha de tendência
modelo = LinearRegression()
cobrancas = df["cobranca"].values.reshape(-1, 1)
sucesso = df["sucesso_acumulado"].values
modelo.fit(cobrancas, sucesso)
trend = modelo.predict(cobrancas)
plt.plot(df["cobranca"], trend, color="red", linestyle="--", label="Linha de Tendência")

# Configurar o gráfico
plt.title("Evolução da Performance do Atleta", fontsize=16)
plt.xlabel("Número da Cobrança", fontsize=12)
plt.ylabel("Taxa de Sucesso Acumulada (%)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Calcular melhoria percentual do início ao fim
melhoria = sucesso[-1] - sucesso[0]
relatorio = f"""
=== Relatório de Evolução ===

Resumo:
- Início: Taxa de sucesso de {sucesso[0]:.2f}%.
- Fim: Taxa de sucesso de {sucesso[-1]:.2f}%.
- Melhoria ao longo do tempo: {melhoria:.2f}%. 

Insights:
- O atleta está {"melhorando" if melhoria > 0 else "mantendo" if melhoria == 0 else "regredindo"} sua performance com o treino.

Intervalos Ideais das Variáveis:
1. Distância: Entre {distancia_range[0]:.1f} e {distancia_range[1]:.1f} metros.
2. Ângulo: Entre {angulo_range[0]:.1f}° e {angulo_range[1]:.1f}°.
3. Altura: Entre {altura_range[0]:.1f}m e {altura_range[1]:.1f}m.
4. Velocidade: Entre {velocidade_range[0]:.1f}m/s e {velocidade_range[1]:.1f}m/s.

Recomendações:
- Foque nos intervalos ideais para maximizar a performance.
- Continue monitorando os resultados para ajustes contínuos no treino.
"""

# Salvar o gráfico como imagem na raiz do projeto
plt.tight_layout()
plt.savefig("grafico.png", dpi=300)  # Salvar na raiz do projeto

# Criar o PDF com o gráfico e o relatório
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Inserir o gráfico no PDF
pdf.image("grafico.png", x=10, y=10, w=190)

# Adicionar o relatório abaixo do gráfico
pdf.ln(150)  # Ajustar a posição do texto abaixo do gráfico
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 10, relatorio)

# Salvar o PDF final na raiz do projeto
pdf.output("relatorio_performance.pdf")

# Exibir a mensagem final
print("PDF gerado com sucesso. Você pode acessar o arquivo 'relatorio_performance.pdf' na raiz do seu projeto.")
