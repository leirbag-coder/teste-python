
# ------------------------------------------------------
#               ENTRADA E SAÍDA DE DADOS
# ------------------------------------------------------

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Olá,", nome)
print(f"Você tem, {idade} anos")



# -----------------------------------------------------
#              CALCULADORA SIMPLES (SOMA)
# -----------------------------------------------------

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
print("A soma é: ",soma)



# -----------------------------------------------------
#              VERIFICAÇÃO DE MAIORIDADE
# -----------------------------------------------------

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")   

  

# -----------------------------------------------------
#                 NÚMERO PAR OU ÍMPAR
#  ----------------------------------------------------     

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")    


# ------------------------------------------------------
#                 CONTADOR COM WHILE
# ------------------------------------------------------

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

    
# -------------------------------------------------------
#                   TABUADA COM FOR
# -------------------------------------------------------

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

# ------------------------------------------------------
#                   LISTA DE NOMES
# ------------------------------------------------------



nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Nomes cadastros: ")
print(nomes)



# ------------------------------------------------------
#            CADASTRO (LISTA + DICIONÁRIO)
# ------------------------------------------------------

alunos = []

nome = (input("Nome do aluno: "))
idade= int(input("Idade: "))
nota = float(input("Nota: "))

aluno = {
    "nome": nome,
    "idade": idade,
    "nota" : nota
}

alunos.append(aluno)

print("Aluno cadstrados:")
print(alunos)

 

# -----------------------------------------------------
#                   FUNÇÃO SIMPLES
# -----------------------------------------------------

def saudacao(nome):
    print("Olá,", nome)

saudacao("Maria")
saudacao("João")


# -----------------------------------------------------
#             FUNÇAÕ COM RETORNO (SOMA)
# -----------------------------------------------------

def soma(a, b):
    return a + b 
resultado = soma(5, 3)
print("Resultado:", resultado)

resultado = soma(7, 13)
print("Resultado:",resultado)

"""

# ----------------------------------------------------
#                JOGO DE ADVINHAÇÃO
# ----------------------------------------------------

import random

numero_secreto = random.randint(1, 10)

while True:
    chute = int(input("Digite um número entre 1 e 10: "))

    if chute == numero_secreto:
        print("Você acertou!")
        break
    else:
        print("Tente novamente")
