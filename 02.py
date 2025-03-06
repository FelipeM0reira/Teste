"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def verifica_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return f"O número {numero} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {numero} NÃO pertence à sequência de Fibonacci."

# Solicita ao usuário que insira um número
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

resultado = verifica_fibonacci(numero)
print(resultado)