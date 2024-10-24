
# Python
# @PauloCastro


# Propt - Questão Exercicio 3
1.Solicte ao usuario que insira uma quantidade determinada de numeros
2. Solicite ao usuario que insira um valor de referencia
3. Use um laço for para verificar quais numeros da lista são maiores que o valor da referencia
4. Exiba os números que atendem a condicao




Claro! Vamos fazer um passo a passo para resolver isso. Aqui está um exemplo de como você pode implementar esse algoritmo em Python:

python
Copiar código
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
Explicação:
Quantidade de Números: O usuário informa quantos números ele vai inserir.
Lista de Números: Um laço for coleta os números e os armazena em uma lista.
Valor de Referência: O usuário insere um valor que será usado para comparação.
Verificação: Outro laço for verifica e imprime os números que são maiores que o valor de referência.
