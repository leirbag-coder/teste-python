import random

numero_secreto = random.randint(1, 10)

chute = int(input("Advinhe qual o número de 0 à 10!"))

if chute == numero_secreto:
    print("Parabéns você acertou!")
elif chute > numero_secreto:
    print("Você errou! O número secreto era Menor!")    
elif chute < numero_secreto:   
    print("Você errou! O número secreto era Maior!") 

segundo_chute = int(input("Segunda tentativa para Advinhar qual o número de 0 à 10!")) 

if segundo_chute == numero_secreto:
    print("Você Acertou!")
else:
    print(f"Você errou! O número era {numero_secreto}")
        