import random

print("Salut, c'est quoi ton nom ")
name = input()
print("Super " + str(name) + ", choisis un nombre ! ")

number = random.randint(1, 20)
##print('DEBUG ' + str(number))
choice = None
cpt = 0

while choice != number:
    choice = int(input())
    if choice < number:
        print('Trop petit !! Re-choisis un nombre :')
        cpt += 1
    elif choice > number:
        print('Trop grand !! Re-choisis un nombre :')
        cpt += 1
    elif choice == number:
        print('Bravo ' + str(name) + ', tu as trouvé en ' + str(cpt) + ' fois !')