from prints import *
from Adaugare import *


def filtre():
    menu_for_5()

    try:
        option_5 = int(input("Selectati comanda filtre:"))
        if option_5 == 1:
            cheltuiala = input("Introduceti cheltuiala:")
            try:
                print(eliminare_cheltuieli(cheltuiala, apartamente))
            except:
                invalid_input()
        elif option_5 == 2:
            suma = int(input("Introduceti suma:"))
            try:
                print(cheltuieli_mai_mici(suma, apartamente))
            except:
                invalid_input()

        elif option_5 == 2:
            pass
        else:
            invalid_input()

    except ValueError:
        invalid_input()


def cheltuieli_mai_mici(suma, my_dict):
    """
    afiseaza toate cheltuielile mai mari decat o suma data
    """
    lista = []
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[1] > suma:
                lista.append(chl[1])
    return lista


def eliminare_cheltuieli(cheltuiala, my_dict):
    """
    afiseaza toate cheltuielile diferite de cea data
    """

    lista = []
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[0] != cheltuiala:
                lista.append(chl[0])
    return lista
