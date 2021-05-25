from prints import *
from Adaugare import *
from Stergere import *
from Cautari import *
from Rapoarte import *
from teste import run_all_test
from Filtre import *
from Undo import *


def run():
    """
    Implement the UI
    """
    printMenu()
    global apartamente
    apartamente.clear()
    true = True
    while true:
        try:
            user = int(input("Selectati comanda meniu:"))
            if user == 1:
                adaugare()
            elif user == 2:
                stergere()
            elif user == 3:
                cautari()
            elif user == 4:
                rapoarte()
            elif user == 5:
                filtre()
            elif user == 6:
                undo()
            elif user == 7:
                print_apart(apartamente)
            elif user == 8:
                true = False
            else:
                invalid_input()

        except ValueError:

            invalid_input()


def undo():
    menu_for_6()
    global apartamente
    apartamente.clear()
    option_6 = int(input("Selectati comanda undo:"))
    try:
        if option_6 == 1:
            try:
                s_pop()
                recreate_ap()
                print_apart(apartamente)
            except:
                stergeri_invalide()
        elif option_6 == 2:
            pass
        else:
            invalid_input()
    except ValueError:
        invalid_input()


def recreate_ap():
    global apartamente
    global stiva

    l = len(stiva)
    if l == 0:
        apartamente.clear()
    else:
        for key in stiva[-1]:
            apartamente[key] = []

        for key in stiva[-1]:
            for lista_mica in stiva[l - 1][key]:
                pls = []
                pls.append(lista_mica[0])
                pls.append(lista_mica[1])
                pls.append(lista_mica[2])
                apartamente[key].append(pls)


def stergere():
    """
    Implement the  UI for the Stergere option

    """
    menu_for_2()

    try:
        option_2 = int(input("Selectati comanda stergere:"))
        if option_2 == 1:
            curatare_stack()
            care = input("Selectati apartamentul:")
            try:
                stergere_cheltuieli(care, apartamente)
                print_apart(apartamente)
                add_to_stack(care)
            except:
                invalid_input()
            creare_stiva_sterge()
        elif option_2 == 2:
            curatare_stack()
            primul = int(input("Introduceti primul numar:"))
            second = int(input("Introduceti al doilea numar:"))
            try:
                stergeri_consecutive(primul, second, apartamente)
                print_apart(apartamente)
                add_to_stack(primul)
                add_to_stack(second)
            except:
                invalid_input()
            create_stiva_consecitive()
        elif option_2 == 3:
            curatare_stack()
            tip = input("Introduceti tipul cheltuielii:")
            try:
                stergere_cheltuiala_specifica(tip, apartamente)
                print_apart(apartamente)
            except:
                invalid_input()
            add_to_stack(tip)
            create_stiva_specifica()
        elif option_2 == 4:
            pass
        else:
            invalid_input()

    except ValueError:
        invalid_input()


run_all_test()
run()
