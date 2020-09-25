import random
import math

choice = -1
mise = -1
money = 500

print("")
print("Bienvenue au casino")
print("Vous avez 500$")

while money > 0:
    print("")
    print("---------------------")
    print("Choississez un nombre entre 0 et 49 inclus :")
    choice = int(input())
    print("")

    while choice > 49 or choice < 0:
        print("Veuillez choisir un nombre ENTRE 0 et 49 inclus :")
        choice = int(input())
        print("")

    while mise > money or mise < 0:
        print("Veuillez choisir une mise à mettre :")
        mise = int(input())
        print("")
    
    money = money - mise

    print("La bille tombe sur .... ")
    number = random.randrange(50)
    print(">> " + str(number) + " <<")
    print("")

    if(number == choice):
        print("-> Victoire (récompense x 3 !)")
        money = money + mise * 3
        print("")
        print("Argent : " + str(money))

        
    if(number%2 == choice%2):
        print("-> Victoire par couleur (récompense * 1.5 !)")
        money = money + math.ceil(mise * 1.5)
        print("")
        print("Argent : " + str(money))

    if(number%2 != choice%2):
        print("-> Défaite")
        print("")
        print("Argent : " + str(money))

    mise = -1
print("Morale : Ne va pas au casino.")