def calcule():
    nombre1 = input("Entrez le premier nombre : ") #demande a utilisateur de donner deux nombre
    nombre2 = input("Entrez le deuxième nombre : ")

    # Vérifier si les valeurs saisies sont des nombres.
    if not (nombre1.isnumeric() and nombre2.isnumeric()):
        raise SystemExit("Fin du programme")

    # Convertir les nombres en entiers.
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

    # Obtenir l'opération souhaitée de l'utilisateur.
    operation = input("Entrez une opération (+, -, * ou /) : ")

    # Vérifier si l'opération est valide.
    if operation not in ["+", "-", "*", "/"]:
        raise SystemExit("Fin du programme")

    # Effectuer le calcul.
    if operation == "+":
        resultat = nombre1 + nombre2
    elif operation == "-":
        resultat = nombre1 - nombre2
    elif operation == "*":
        resultat = nombre1 * nombre2
    elif operation == "/":
        if nombre2 == 0:  # Vérifier la division par zéro.
            raise SystemExit("Impossible de diviser par 0. Fin du programme")
        resultat = round(nombre1 / nombre2, 2)  # Arrondir le résultat.

    # Afficher le résultat.
    print(f"Le résultat de l'opération est :", {resultat})