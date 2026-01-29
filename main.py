"""
print("olá mundo")
nome = input("qual seu nome ?")
idade = int(input("qual sua idade?"))
a = int(input("digie um número para a?"))
b = int(input("digite um número para b?"))


maioridade = ""
if idade >= 21:
    maioridade = "Maior de 21 anos!"
elif idade >= 18:
    maioridade = "Maior ou igual de 18 anos!"
else:
    maioridade = "Menor de 18 anos!"    

def somar(a,b):
    return a + b 
print(f"o resultado da conta a + b = {somar(a,b)}")


print(f"olá {nome}, você tem {idade} anos! Pelo visto você tem idade {maioridade}!") 

for i in range(5):
    print(f"Valor de i é igual à: {i}")
"""

frutas = ["Maçã", "Banana", "Uva"]


frutas.append("pera")       # Adiciona um item ao final
frutas.remove("Banana")     # Remove um item específico
frutas.insert(1, "laranja") # Adiciona em uma posição específica
print(len(frutas))          # Quantos itens tem na lista
for frutas in frutas:
    print("Eu gosto de ", frutas)