#Crie um jogo onde o computador escolhe um número entre 1 e 100 e o usuário tenta adivinhar. 
#Dê dicas ("maior", "menor") até acertar. Use random.randint(), while e input().

import random

print("=== Jogo de Adivinhação ===")

while True:
    numero = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = int(input("Adivinhe um número de 1 a 100: "))
        tentativas += 1

        if palpite == numero:
            print(f"Parabéns! Você acertou em {tentativas} tentativas! 🎉")
            break
        elif palpite < numero:
            print("O número é MAIOR.")
        else:
            print("O número é MENOR.")

    jogar = input("Quer jogar novamente? (s/n): ").lower()
    if jogar != "s":
        print("Obrigado por jogar! 👋")
        break
