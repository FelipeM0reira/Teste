"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverter_string(texto: str) -> str:
    return ''.join(texto[i] for i in range(len(texto) - 1, -1, -1))

def main():
    texto_original = input("Digite uma string para inverter: ")

    if not texto_original:
        print("A string está vazia. Por favor, insira uma string válida.")
        return

    texto_invertido = inverter_string(texto_original)

    print(f"String original: {texto_original}")
    print(f"String invertida: {texto_invertido}")

if __name__ == "__main__":
    main()