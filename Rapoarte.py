from prints import *
from Adaugare import *
from Stergere import *
from Cautari import *


def rapoarte():
    """
    Implement the  UI for the Rapoarte option
    """

    menu_for_4()
    try:
        option_4 = int(input("Selectati comanda rapoarte:"))
        if option_4 == 1:
            tip = input("Introduceti tipul cheltuielii:")
            try:
                print(suma_tot_cheltuiala(tip, apartamente))
            except:
                invalid_input()
        elif option_4 == 2:
            cheltuiala = input("Introduceti cheltuiala:")
            try:
                print(sortare_apartamente(cheltuiala, apartamente))
            except:
                invalid_input()
        elif option_4 == 3:
            care = input("Introduceti apartamentul:")
            try:
                print(suma_cheltuieli_apartament(care, apartamente))
            except:
                invalid_input()
        elif option_4 == 4:
            pass
        else:
            invalid_input()

    except ValueError:
        invalid_input()


def suma_tot_cheltuiala(tip, my_dict):
    """
    returneaza suma tuturor cheltuielilor de acelasi tip introdusa de user 
    """
    suma = 0
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[0] == tip:
                suma += chl[1]
    return suma


def suma_cheltuieli_apartament(care, my_dict):
    """
    returneaza suma tutuor cheltuielilor  de la un apartament introdus de user
    """
    suma = 0
    for key in my_dict:
        if care == key:
            for chl in my_dict[key]:
                suma += chl[1]
    return suma


def sortare_apartamente(cheltuiala, my_dict):
    """
    pune intr-o lista apartamentele sortate dupa o anumita cheltuiala
    """
    lista = []
    lista2 = []
    for key in my_dict:
        for chl in my_dict[key]:
            if cheltuiala == chl[0]:
                lista.append(chl[1])

    lista.sort()
    for x in lista:
        ok = 0
        for key in my_dict:
            for chl in my_dict[key]:
                if chl[1] == x:
                    lista2.append(key)
                    ok = 1
                    break
            if ok == 1:
                break

    return lista2
