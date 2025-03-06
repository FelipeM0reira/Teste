"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

def analise_faturamento(dados):
    # Filtra dias com faturamento
    faturamento_valido = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    # Calcula o menor e o maior valor de faturamento
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    
    # Calcula a média mensal (ignorando dias sem faturamento)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    
    # Conta dias acima da média
    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

# Lê o arquivo JSON
try:
    with open('dados.json', 'r') as file:
        dados_faturamento = json.load(file)

    # Realiza a análise
    menor, maior, dias_acima = analise_faturamento(dados_faturamento)

    # Imprime os resultados
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")

except FileNotFoundError:
    print("Erro: O arquivo 'dados.json' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: O arquivo 'dados.json' não contém um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")