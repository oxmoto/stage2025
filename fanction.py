valeur = {
    "nbr_host": 0,
    "host_core": 20,
    "host_RAM": 512,
    "VM_core": 2,
    "VM_RAM": 4
}

def get_host_number():
    nbr_host = 0
    while nbr_host <= 1:
        try:
            nbr_VM = input("Entrez le nombre de VM qui a dans le(s) serveur(s) ( en chiffre, min 2 ) : ")
            nb_VM_core = nbr_VM * 2
            nb_VM_RAM = nbr_VM * 4
            total_core= int(nb_VM_core) / 20
            total_RAM = int(nb_VM_RAM) / 512
            total_core = total_core * 0.8
            total_RAM = total_RAM * 0.8
            total_core = int(total_core)
            total_RAM = int(total_RAM)
            if total_core <= total_RAM :
                print(f"vois si combien il y a de host {total_RAM}")
            if total_core >= total_RAM :
                print(f"vois si combien il y a de host {total_core}")
        except ValueError as err:
            print("Vous n'avez pas entré un nombre!")
            continue
    return nbr_host


# fonction calculate
def calculate(nbr_host_core, nbr_host_RAM, nbr_VM_core, nbr_VM_RAM, nbr_nbr_host):
    cluster_ram = nbr_host_RAM * nbr_nbr_host
    cluster_core = nbr_host_core * nbr_nbr_host
    nbr_vm_ram = int(cluster_ram / nbr_VM_RAM)
    nbr_vm_core = int(cluster_core / nbr_VM_core)
    if nbr_vm_ram <= nbr_vm_core:
        return nbr_vm_ram
    elif nbr_vm_core <= nbr_vm_ram:
        return nbr_vm_core

# fonction main
def main():
    cluster_size = get_host_number()
    resultat = calculate(valeur["host_core"], valeur["host_RAM"], valeur["VM_core"], valeur["VM_RAM"], cluster_size)
    resultat = resultat * 0.8
    print(f"vois si le nombre de VM que tu peux mettre dans ton cluster :{int(resultat)}")

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
    print(f"Le résultat de l'opération est :", resultat)

def memu(liste_string):
    """
    qu'est-ce que ça fait
    :param liste_string: liste de chaine de caracteres
    :return: la chaine selectioné
    """
    nbr_entry = 0
    chois_int = -1
    if len(liste_string) <= 0:
        return 'exit'
    for entry in liste_string:
       nbr_entry += 1
       print(f'{nbr_entry} - {entry}')
    print('0 - Exit')
    while 0 > chois_int or nbr_entry < chois_int:
        chois_int = int(input("Quel est votre chois?"))
    if 0 > chois_int or nbr_entry < chois_int:
        print(f"Merci de choir une valeur entre 0 et {nbr_entry}!")
    if chois_int == 0:
     return 'exit'
    else:
        return liste_string[chois_int - 1]

get_host_number()