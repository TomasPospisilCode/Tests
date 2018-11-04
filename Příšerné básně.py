import random

def funkce():
    pocetRadku = 5

    while(True):
        try:
            noveCislo = int(input("Enter number between 1-10(including): "))
            if 1<= noveCislo <= 10:
                pocetRadku = noveCislo
                break
            else:
                print("You have to enter number in range 1-10")

        except Exception as e: print(e)



    zajmena = ["my", "yours", "her's", "his"]
    podstatnaJmena= ["Trump", "rum", "idiot", "Hilary", "dog", "cat", "policeman"]
    slovesa = ["whistles", "plays", "sleeps", "drinks", "says", "fly", "heals"]
    prislovce = ["tasty", "nicely", "lightly", "slowly", "boringly"]
    for item in range(pocetRadku):
        print(random.choice(zajmena), random.choice(podstatnaJmena),random.choice(slovesa), random.choice(prislovce))

funkce()
