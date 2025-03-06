"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
"""

from typing import Dict
from decimal import Decimal, ROUND_HALF_UP

def calcular_percentuais(faturamento: Dict[str, float]) -> Dict[str, Decimal]:
    total = sum(faturamento.values())
    return {
        estado: (Decimal(valor) / Decimal(total) * 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        for estado, valor in faturamento.items()
    }

def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    percentuais = calcular_percentuais(faturamento)

    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual}%")

if __name__ == "__main__":
    main()