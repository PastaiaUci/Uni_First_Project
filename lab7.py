from prints import *
from Adaugare import *
from Cautari import *
from Undo import *
apart = {}
new_list = []


def run():
    """
    Implement the UI
    """
    printMenu_lab()
    true = True
    while true:
        user = input("Selectati comanda meniu:")
        if user == "6":
            break
        global apart
        lista_comenzi = user.split(",")
        for x in lista_comenzi:
            new_list.append(x.split(" "))
        for comenzi in new_list:
            if comenzi[0] == "1" and comenzi[1] == "1":
                try:
                    curatare_stack()
                    adaugare_apartament(comenzi[2], apart)
                    add_to_stack("Apartamentul " + comenzi[2])
                    create_stiva_adaugare()
                except:
                    print("Comanda adaugari invalida!")
            elif comenzi[0] == "1" and comenzi[1] == "2":
                try:
                    curatare_stack()
                    adaugare_cheltuiala(
                        "Apartamentul " + str(comenzi[2]), comenzi[3], comenzi[4], comenzi[5], apart)
                    add_to_stack("Apartamentul " + comenzi[2])
                    add_to_stack(comenzi[3])
                    add_to_stack(comenzi[4])
                    add_to_stack(comenzi[5])
                    create_stiva_adaugare_chl()
                except:
                    print("Comanda modificari invalida!")
            elif comenzi[0] == "2":
                try:
                    curatare_stack()
                    stergere_cheltuieli(
                        "Apartamentul " + str(comenzi[2]), apart)
                    add_to_stack("Apartamentul " + str(comenzi[2]))
                    creare_stiva_sterge()
                except:
                    print("Comanda stergeri invalida!")

            elif comenzi[0] == "3":
                try:
                    print(cheltuieli_mai_mari(comenzi[2], apart))
                except:
                    print("Comanda cautari invalida!")
            elif comenzi[0] == "6" and comenzi[1] == "1":
                try:
                    s_pop()
                    apart = return_last()
                except:
                    stergeri_invalide()
            elif comenzi[0] == "6" and comenzi[1] != "1":
                print("Comanda undo invalida!")
            print(apart)

        lista_comenzi.clear()
        new_list.clear()
        print(apart)


run()
