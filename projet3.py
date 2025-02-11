

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
    if chois_int==0:
        return 'exit'
    else:
        return liste_string[chois_int-1]


list_chois = ["chois1", "chois2", "chois3", "chois4"]
chois = memu(list_chois)
if chois == "chois1":
    print("Coucou1")
elif chois == "chois2":
    print("Coucou2")
elif chois == "chois3":
    print("Coucou3")
elif chois == "chois4":
    print("Coucou4")
else:
    print("exit")
"""
Menu
1- chois1
2- Chois2
3- Chois3
4- chois4
0- exit
Que voulez vous faire?
len(list_chois)
Appel:
list_chois=["chois1","chois2"...]
chois=memu(list_chois)
if chois == "chois1":
    print("chois1")
elif chois == "chois2":
    print("chois2")
elif chois == "chois3":
    print("chois3")
elif chois == "chois4":
    print("chois4")
else:
    print("exit")
"""
