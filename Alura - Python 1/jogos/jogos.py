import forca
import adivinhacao

print("*************************************")
print("Escolha o seu jogo")
print("*************************************")

print("(1) Jogo da Forca \n(2) Jogo da Adivinhação")
jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar()
    