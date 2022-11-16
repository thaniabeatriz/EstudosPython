import random

def jogar():

    print("*************************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*************************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade você quer?")
    print("\nNível 1 - fácil\nNível 2 - Médio\nNível 3 - Difícil")
    nivel = int(input("\nDigite o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas+1)  : 
        print("\nRodada {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 101):
            print("Você deve digitar um número entre 1 e 100!")    
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior que o numero secreto")
            elif(menor):
                print("Voce errou! O seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")
    
if (__name__ == "__main__"):
    jogar()