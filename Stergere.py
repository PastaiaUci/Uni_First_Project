from prints import *
from Undo import *
from Adaugare import *


def stergere_cheltuieli(care, my_dict):
    """
    sterge toate cheltuielile dintr-un apartament dat
    """
    for key in my_dict:
        if care == key:
            my_dict[key].clear()


def stergeri_consecutive(primul, second, my_dict):
    """
    stergerea cheltuielilor pentru apartamente consecutive
    """

    for key in my_dict:
        if int(key.split()[1]) >= primul and int(key.split()[1]) <= second:
            my_dict[key].clear()


def stergere_cheltuiala_specifica(tip, my_dict):
    """
    Șterge cheltuielile de un anumit tip de la toate apartamentele
    """
    for key in my_dict:
        for chl in my_dict[key]:
            if chl[0] == tip:
                my_dict[key].remove(chl)
