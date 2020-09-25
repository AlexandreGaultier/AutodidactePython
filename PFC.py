import random

print('Pierre Feuille Ciseaux')
print('Entrez votre nom :')
name = input()

Jpoints = 0
Opoints = 0
end = 0
while end == 0:
    Ochoix = random.randint(1, 3)
    print('Choisissez : 1 (Pierre), 2 (Feuille) ou 3 (Ciseaux)')
    Jchoix = int(input())

    if Jchoix == 1 and Ochoix == 3:
        print('Pierre vs Ciseaux')
        print(str(name) + " l'emporte")
        Jpoints += 1
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')
    
    if Jchoix == 2 and Ochoix == 1:
        print('Feuille vs Pierre')
        print(str(name) + " l'emporte")
        Jpoints += 1
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')

    if Jchoix == 3 and Ochoix == 2:
        print('Ciseaux vs Feuille')
        print(str(name) + " l'emporte")
        Jpoints += 1
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')

    if Jchoix == 3 and Ochoix == 1:
        print('Ciseaux vs Pierre')
        print("L'Ordinateur l'emporte")
        Opoints += 1
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')
    
    if Jchoix == 1 and Ochoix == 2:
        print('Pierre vs Feuille')
        print("L'Ordinateur l'emporte")
        Opoints += 1
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')

    if Jchoix == 2 and Ochoix == 3:
        print('Feuille vs Ciseaux')
        print("L'Ordinateur l'emporte")
        Opoints += 1
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')
    
    if Jchoix == 1 and Ochoix == 1:
        print('Pierre vs Pierre')
        print('Egalité')
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')
    
    if Jchoix == 2 and Ochoix == 2:
        print('Feuille vs Feuille')
        print('Egalité')
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')
    
    if Jchoix == 3 and Ochoix == 3:
        print('Ciseaux vs Ciseaux')
        print('Egalité')
        print('---' + str(Jpoints) + '---' + str(Opoints) + '---')
        
    if Jpoints == 5:
        print('Vicoire pour ' + str(name) + ' !! ' + str(Jpoints) + ' à ' +str(Opoints))
        end = 1
    if Opoints == 5:
        print('Vicoire pour Ordinateur !! ' + str(Opoints) + ' à ' +str(Jpoints))
        end = 1