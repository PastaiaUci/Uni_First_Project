from prints import *
from Undo import *
from Stergere import *

apartamente = {}
li = []


def adaugare():
    """
    Implement the  UI for the Adauga option
    """

    menu_for_1()
    try:
        option_1 = int(input("Selectati comanda adaugare:"))
        if option_1 == 1:
            curatare_stack()
            id_ap = int(
                input("Introduceti numarul apartamentului pe care doriti sa il adaugati:"))
            if id_ap > 0:
                adaugare_apartament(id_ap, apartamente)
                print_apart(apartamente)
                add_to_stack("Apartamentul " + str(id_ap))
                create_stiva_adaugare()
            else:
                print("Numarul apartamentului trebuie sa fie >0")

        elif option_1 == 2:
            curatare_stack()
            care = input("Selectati  apartamentul:")
            tip = input("Introduceti tipul cheltuielii:")
            suma = int(input("Introduceti suma cheltuielii:"))
            zi = int(input("Introduceti ziua cheltuielii:"))
            try:
                adaugare_cheltuiala(care, tip, suma, zi, apartamente)

            except:
                inexistent()
            add_to_stack(care)
            add_to_stack(tip)
            add_to_stack(suma)
            add_to_stack(zi)
            create_stiva_adaugare_chl()
            print_apart(apartamente)

        elif option_1 == 3:
            curatare_stack()
            care = input("Selectati  apartamentul:")
            tip = input("Introduceti tipul cheltuielii:")
            suma = int(input("Introduceti noua suma:"))

            try:
                modificare_cheltuiala(care, tip, suma, apartamente)

            except:
                inexistent()
            add_to_stack(care)
            add_to_stack(tip)
            add_to_stack(suma)
            create_stiva_modificare()
            print_apart(apartamente)

        elif option_1 == 4:
            pass
        else:
            invalid_input()

    except ValueError:
        invalid_input()


def adaugare_apartament(id, my_dict):
    """
    adauga un apartament in dictionar
    """
    my_dict["Apartamentul " + str(id)] = []


def adaugare_cheltuiala(care, tip, suma, zi, my_dict):
    """
    adaugarea unei cheltuieli introdusa de user
    """
    my_list = []
    my_list.append(tip)
    my_list.append(suma)
    my_list.append(zi)
    my_dict[care].append(my_list)


def modificare_cheltuiala(care, tip, suma, my_dict):
    """
    Modifica o cheltuiala introdusa de utilizator;
    Cauta tipul cheltuielii si schimba valoare in cea dorita;
    """
    for key in my_dict:
        if care == key:
            for chl in my_dict[key]:
                if chl[0] == tip:
                    chl[1] = suma
