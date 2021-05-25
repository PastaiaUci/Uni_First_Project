from prints import *
from Adaugare import *


myStack = []
stiva = []


def return_last():
    """
    dictionarul revine la forma precedenta
    """
    if len(stiva) == 0:
        return {}
    else:
        return stiva[-1]


def s_pop():
    """
    elimina ultimul element din stiva
    """
    del stiva[-1]


def add_to_stack(item):
    """
    adauga un itme in stiva
    """
    myStack.append(item)


def curatare_stack():
    """
    sterg toate elementele din stack
    """
    myStack.clear()


def create_stiva_adaugare():
    """
    formeaza in stiva iteratiile vechi ale programului
    """
    if len(stiva) == 0:
        my_dict = {}
        my_dict[myStack[0]] = []

        stiva.append(my_dict)
    else:
        my_dict = {}
        l = len(stiva)

        for x in stiva[l - 1]:
            my_dict[x] = []

        for key in stiva[l - 1]:
            for lista_mica in stiva[l - 1][key]:
                pls = []
                pls.append(lista_mica[0])
                pls.append(lista_mica[1])
                pls.append(lista_mica[2])
                my_dict[key].append(pls)

        my_dict[myStack[0]] = []
        stiva.append(my_dict)


def create_stiva_adaugare_chl():
    """
    formeaza in stiva iteratiile vechi ale programului
    """
    my_dict = {}
    l = len(stiva)

    for key in stiva[l - 1]:
        my_dict[key] = []

    li = []
    li.append(myStack[1])
    li.append(myStack[2])
    li.append(myStack[3])

    for key in stiva[l - 1]:
        for lista_mica in stiva[l - 1][key]:
            pls = []
            pls.append(lista_mica[0])
            pls.append(lista_mica[1])
            pls.append(lista_mica[2])
            my_dict[key].append(pls)

    for key in my_dict:
        if key == myStack[0]:
            my_dict[key].append(li)
            break
    stiva.append(my_dict)


def create_stiva_modificare():
    """
    formeaza in stiva iteratiile vechi ale programului
    """
    my_dict = {}
    l = len(stiva)

    for key in stiva[l - 1]:
        my_dict[key] = []

    for key in stiva[l - 1]:
        for lista_mica in stiva[l - 1][key]:
            pls = []
            pls.append(lista_mica[0])
            pls.append(lista_mica[1])
            pls.append(lista_mica[2])
            my_dict[key].append(pls)

    for key in my_dict:
        if key == myStack[0]:
            for chl in my_dict[key]:
                if chl[0] == myStack[1]:
                    chl[1] = myStack[2]

    stiva.append(my_dict)


def creare_stiva_sterge():
    my_dict = {}
    l = len(stiva)

    for key in stiva[l - 1]:
        my_dict[key] = []

    for key in stiva[l - 1]:
        for lista_mica in stiva[l - 1][key]:
            pls = []
            pls.append(lista_mica[0])
            pls.append(lista_mica[1])
            pls.append(lista_mica[2])
            my_dict[key].append(pls)

    for key in my_dict:
        if myStack[0] == key:
            my_dict[key].clear()

    stiva.append(my_dict)


def create_stiva_consecitive():
    my_dict = {}
    l = len(stiva)

    for key in stiva[l - 1]:
        my_dict[key] = []

    for key in stiva[l - 1]:
        for lista_mica in stiva[l - 1][key]:
            pls = []
            pls.append(lista_mica[0])
            pls.append(lista_mica[1])
            pls.append(lista_mica[2])
            my_dict[key].append(pls)

    for key in my_dict:
        if int(key.split()[1]) >= myStack[0] and int(key.split()[1]) <= myStack[1]:
            my_dict[key].clear()

    stiva.append(my_dict)


def create_stiva_specifica():
    my_dict = {}
    l = len(stiva)

    for key in stiva[l - 1]:
        my_dict[key] = []

    for key in stiva[l - 1]:
        for lista_mica in stiva[l - 1][key]:
            pls = []
            pls.append(lista_mica[0])
            pls.append(lista_mica[1])
            pls.append(lista_mica[2])
            my_dict[key].append(pls)

    for key in my_dict:
        for chl in my_dict[key]:
            if chl[0] == myStack[0]:
                my_dict[key].remove(chl)

    stiva.append(my_dict)
