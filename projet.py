#!/bin/env python3

from fanction import memu
from fanction import main
from fanction import calcule
from fanction import get_host_number1

def handle_memu():
    while True:
        list_chois = ["calcule", "taille_VM", "taille_hosts"]
        chois = memu(list_chois)
        if chois == "calcule":
            calcule()
            return
        if chois == "taille_VM":
            main()
            return
        if chois == "taille_hosts":
            get_host_number1()
            return
        if chois == "exit":
            exit()

handle_memu()

"""
Programe de calcul de ressource de virtualisation

Fonctions:
- memu
- calcule
- mise à jour parametres
- lecture de fichier json (parametre)
- ecriture de json (parametre)

Menus:
principale:
- Calule
- Taille hosts
- taille VM moyenne
- exit (sort du programme)

Hosts:
- Nbr core
- taille ram
- exit (revien au menu principale)

VM:
- nbr core
- taille ram
- exit (revien au menu principale)

utiliser boucle while avec une var run initialise a True
"""

if __name__ == '__main__':
    main()
