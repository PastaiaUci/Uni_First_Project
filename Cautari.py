from prints import *
from Adaugare import *
from Stergere import *


def cautari():
    """
    Implement the  UI for the Cautari option
    """
    menu_for_3()
    try:
        option_3 = int(input("Selectati comanda cautari:"))
        if option_3 == 1:
            suma = int(input("Introduceti suma:"))
            try:
                print(cheltuieli_mai_mari(suma, apartamente))
            except:
                inexistent()
        elif option_3 == 2:
            tip = input("Selectati tipul cheltuielii:")
            try:
                print(cheltuieli_de_acelasi_tip(tip, apartamente))
            except:
                inexistent()
        elif option_3 == 3:
            suma = int(input("Introduceti suma:"))
            ziua = int(input("Introduceti ziua:"))
            try:
                print(cheltuieli_inainte_de_zi(suma, ziua, apartamente))
            except:
                invalid_input()
        elif option_3 == 4:
            pass
        else:
            invalid_input()

    except ValueError:
        invalid_input()


def cheltuieli_mai_mari(suma, my_dict):
    """
    cauta si tipareste toate apartamentele ce respecta proprietatea
    """
    lista = []
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[1] > suma:
                lista.append(key)

    return lista


def cheltuieli_de_acelasi_tip(tip, my_dict):
    """
    cauta si tipareste suma cheltuielii(introdusa de user) de la toate apartamentele 
    """
    lista = []
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[0] == tip:
                lista.append(chl[1])
    return lista


def cheltuieli_inainte_de_zi(suma, ziua, my_dict):
    """
    cauta apartamentul si cheltuiala care respecta proprietatea data
    """
    lista = []
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[1] > suma and chl[2] < ziua:
                lista.append(key)
                lista.append(chl[1])

    return lista
