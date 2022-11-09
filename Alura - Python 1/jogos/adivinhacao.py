print("*************************************")
print("Bem vindo ao jogo de adivinhação")
print("*************************************")

numero_secreto = 42
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    
    print("\nRodada {} de {}".format(rodada, tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Voce acertou!")
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce errou! O seu chute foi menor que o numero secreto")
    
    rodada = rodada + 1

print("Fim do jogo!")