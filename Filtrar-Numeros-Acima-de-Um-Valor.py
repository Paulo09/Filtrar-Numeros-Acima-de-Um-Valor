# Passo 1: Solicitar ao usuário que insira a quantidade de números
quantidade = int(input("Quantos números você deseja inserir? "))

# Passo 2: Criar uma lista para armazenar os números
numeros = []

# Solicitar ao usuário que insira os números
for i in range(quantidade):
    numero = float(input(f"Insira o número {i + 1}: "))
    numeros.append(numero)

# Passo 3: Solicitar ao usuário que insira um valor de referência
valor_referencia = float(input("Insira um valor de referência: "))

# Passo 4: Verificar quais números são maiores que o valor de referência e exibir
print("Números maiores que o valor de referência:")
for numero in numeros:
    if numero > valor_referencia:
        print(numero)
