#!/bin/env python
"""
Menus:
principale:
- Calule
- Taille hosts
- taille VM moyenne

Hosts:
- Nbr core
- taille ram

VM:
- nbr core
- taille ram

runstate = True
while runstate:
    ....
    if choice == "extit":
        runstate = False
"""
# Variables
valeur = {
    "nbr_host": 0,
    "host_core": 20,
    "host_RAM": 512,
    "VM_core": 2,
    "VM_RAM": 4
}

# fonction get_host_number
def get_host_number():
    nbr_host = 0
    while nbr_host <= 1:
        try:
             nbr_host = int(input("Entrez le nombre de host  ( en chiffre, min 2 ) : "))

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

