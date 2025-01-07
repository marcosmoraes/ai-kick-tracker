# Análise de Performance de Atletas

Este projeto realiza a análise de desempenho de atletas em um conjunto de dados simulado. Ele calcula a taxa de sucesso acumulada das cobranças, gera um gráfico da evolução da performance do atleta ao longo do tempo, e cria um relatório com insights e recomendações. Além disso, o projeto gera um PDF contendo o gráfico e o relatório.

## Funcionalidades

1. **Carregamento de dados**: O projeto carrega um arquivo JSON contendo os dados das cobranças simuladas.
2. **Análise de performance**: Calcula a taxa de sucesso acumulada ao longo das cobranças.
3. **Gráfico**: Gera um gráfico da evolução da taxa de sucesso acumulada.
4. **Relatório**: Cria um relatório com insights sobre a performance do atleta, incluindo:
   - Resumo da taxa de sucesso no início e no fim do treino.
   - Melhoria ao longo do tempo.
   - Intervalos ideais para variáveis como distância, ângulo, altura e velocidade.
5. **PDF**: O gráfico e o relatório são salvos em um PDF gerado automaticamente.

## Requisitos

Antes de rodar o código, instale as dependências necessárias:

```bash
pip install pandas scikit-learn matplotlib fpdf
