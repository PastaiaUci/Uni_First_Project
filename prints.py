def printMenu_lab():
    """
      Print out the main menu of the application
    """
    print("  Application menu:")
    print("     1.Adaugare")
    print("     2.Stergere")
    print("     3.Cautari")
    print("     6.Exit")


def printMenu():
    """
      Print out the main menu of the application
    """
    print("  Application menu:")
    print("     1.Adaugare")
    print("     2.Stergere")
    print("     3.Cautari")
    print("     4.Rapoarte")
    print("     5.Filtru")
    print("     6.Undo")
    print("     7.Exit")


def menu_for_1():
    """
    print the menu for the first option
    """
    print("1.Doriti sa adaugati un apartament?")
    print("2.Doriti sa adaugati o cheltuiala?")
    print("3.Doriti sa modificati o cheltuiala?")
    print("4.Inapoi")


def menu_for_2():
    """
    print the menu for the second option
    """
    print("1.Șterge toate cheltuielile de la un apartament")
    print("2.Șterge cheltuielile de la apartamente consecutive")
    print("3.Șterge cheltuielile de un anumit tip de la toate apartamentele")
    print("4.Inapoi")


def menu_for_3():
    """
    print the menu for the third option
    """
    print("1.Tipărește toate apartamentele care au cheltuieli mai mari decât o sumă dată")
    print("2.Tipărește cheltuielile de un anumit tip de la toate apartamentele")
    print("3.Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua)")
    print("4.Inapoi")


def menu_for_4():
    """
    print the menu for the fourth option
    """
    print("1.Tipărește suma totală pentru un tip de cheltuială")
    print("2.Tipărește toate apartamentele sortate după un tip de cheltuială")
    print("3.Tipărește totalul de cheltuieli pentru un apartament dat")
    print("4.Inapoi")


def menu_for_5():
    """
    print the menu for the fifth option
    """
    print("1.Elimină toate cheltuielile de un anumit tip")
    print("2.Elimină toate cheltuielile mai mici decât o sumă dată")
    print("4.Inapoi")


def menu_for_6():
    """
    print the menu for the sixth option
    """
    print("1.Reface ultima operație")
    print("4.Inapoi")


def print_apart(my_dict):
    """
    afiseaza dictionarul de apartamente
    """
    print(my_dict)


def invalid_input():
    print("Input invalid")


def inexistent():
    print("Valori inexistente!")


def stergeri_invalide():
    print("Nu se mai pot face undo-uri!")


def comanda_invalida():
    print("Comanda invalida!")
