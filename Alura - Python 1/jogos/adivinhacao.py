print("*************************************")
print("Bem vindo ao jogo de adivinhação")
print("*************************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")
print("Voce digitou ", chute_str)
chute = int(chute_str)

if(numero_secreto == chute):
    print("Voce acertou!")
else:
    print("Voce errou!")
    
print("Fim do jogo!")