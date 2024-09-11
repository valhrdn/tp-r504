import fonctions as f

while True:
    try:
        # Saisie des deux nombres
        a = int(input("Veuillez entrer le premier nombre (base) : "))
        b = int(input("Veuillez entrer le deuxième nombre (exposant) : "))

        # Calcul de la puissance
        resultat = f.puissance(a, b)

        # Affichage du résultat
        print(f"{a} élevé à la puissance {b} est {resultat}")

    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
    except TypeError as e:
        print(e)

