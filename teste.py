from Adaugare import *
from Stergere import *
from Cautari import *
from Rapoarte import *
from Filtre import *
from Undo import *


def test_adaugare_apartament():
    """
    test function for adauga_apartamente()
    """
    dictionar = {}
    new_dictionar = {'Apartamentul 4': []}
    adaugare_apartament(4, dictionar)
    assert dictionar == new_dictionar

    adaugare_apartament(3, dictionar)
    new_dictionar = {'Apartamentul 4': [], 'Apartamentul 3': []}
    assert dictionar == new_dictionar

    adaugare_apartament(3, dictionar)
    assert dictionar == new_dictionar

    adaugare_apartament(32, dictionar)
    new_dictionar = {'Apartamentul 4': [],
                     'Apartamentul 3': [], 'Apartamentul 32': []}

    try:
        dictionar = {}
        new_dictionar = {'Apartamentul 3': []}
        adaugare_apartament(2, dictionar)
        assert dictionar == new_dictionar
        assert False
    except Exception:
        assert True


def test_adaugare_cheltuiala():

    dictionar = {'Apartamentul 1': []}
    new_dictionar = {'Apartamentul 1': [['apa', 12, 1]]}
    adaugare_cheltuiala('Apartamentul 1', 'apa', 12, 1, dictionar)
    assert dictionar == new_dictionar

    adaugare_cheltuiala('Apartamentul 1', 'lumina', 15, 2, dictionar)
    new_dictionar = {'Apartamentul 1': [['apa', 12, 1], ['lumina', 15, 2]]}
    assert dictionar == new_dictionar

    adaugare_cheltuiala('Apartamentul 1', 'lumina', 17, 3, dictionar)
    new_dictionar = new_dictionar = {'Apartamentul 1': [
        ['apa', 12, 1], ['lumina', 15, 2], ['lumina', 17, 3]]}
    assert dictionar == new_dictionar

    adaugare_cheltuiala('Apartamentul 1', 'lumina', 15, 4, dictionar)
    new_dictionar = new_dictionar = {'Apartamentul 1': [
        ['apa', 12, 1], ['lumina', 15, 2], ['lumina', 17, 3], ['lumina', 15, 4]]}
    assert dictionar == new_dictionar

    try:
        adaugare_cheltuiala('Apartamentul 3', 'apa', '12', 1, dictionar)
        adaugare_cheltuiala(43, 'apa', '12', 2, dictionar)
        assert False
    except:
        assert True


def test_modificare_cheltuiala():
    dictionar = {'Apartamentul 1': [['apa', 12]]}
    new_dictionar = {'Apartamentul 1': [['apa', 11]]}
    modificare_cheltuiala('Apartamentul 1', 'apa', 11,  dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], ['lumina', 18]]}
    new_dictionar = {'Apartamentul 1': [['apa', 12], ['lumina', 10]]}
    modificare_cheltuiala('Apartamentul 1', 'lumina', 10,  dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 18]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]]}
    new_dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 18]], 'Apartamentul 4': [['lumina', 120], ['apa', 432]]}
    modificare_cheltuiala('Apartamentul 4', 'lumina', 120,  dictionar)
    assert dictionar == new_dictionar

    try:
        modificare_cheltuiala('Apartametn', 'apa', 120, dictionar)
        modificare_cheltuiala('Apartamentul 1', 'apa', '120', dictionar)
        modificare_cheltuiala('Apartamentul', 'apa', '120', dictionar)
        assert False
    except:
        assert True


def test_stergere_cheltuiala():
    dictionar = {'Apartamentul 1': [['apa', 12]]}
    new_dictionar = {'Apartamentul 1': []}
    stergere_cheltuieli('Apartamentul 1', dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], ['lumina', 134]]}
    new_dictionar = {'Apartamentul 1': []}
    stergere_cheltuieli('Apartamentul 1', dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]]}
    new_dictionar = {'Apartamentul 1': [
        ['apa', 12], ['lumina', 134]], 'Apartamentul 4': []}
    stergere_cheltuieli('Apartamentul 4', dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]]}
    new_dictionar = {'Apartamentul 1': [], 'Apartamentul 4': []}
    stergere_cheltuieli('Apartamentul 4', dictionar)
    stergere_cheltuieli('Apartamentul 1', dictionar)
    assert dictionar == new_dictionar
    try:
        dictionar = {}
        stergere_cheltuieli('ap', dictionar)
        stergere_cheltuieli(1, dictionar)
        stergere_cheltuieli(1, 1)
        assert False
    except:
        assert True


def test_stergeri_consecutive():

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 3': [['apa', 15]]}
    new_dictionar = {'Apartamentul 1': [], 'Apartamentul 3': [['apa', 15]]}
    stergeri_consecutive(1, 2, dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 3': [['apa', 15]]}
    new_dictionar = {'Apartamentul 1': [], 'Apartamentul 3': []}
    stergeri_consecutive(1, 3, dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 3': [['apa', 15]], 'Apartamentul 2': []}
    new_dictionar = {'Apartamentul 1': [],
                     'Apartamentul 3': [], 'Apartamentul 2': []}
    stergeri_consecutive(1, 4, dictionar)
    assert dictionar == new_dictionar

    dicionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    new_dictionar = {'Apartamentul 1': [], 'Apartamentul 4': [
        ['lumina', 150], ['apa', 432]], 'Apartamentul 3': []}
    stergeri_consecutive(1, 3, dicionar)
    assert dicionar == new_dictionar


def test_stergere_cheltuiala_specifica():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    new_dictionar = {'Apartamentul 1': [['lumina', 134]]}
    stergere_cheltuiala_specifica('apa', dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134], ['apa', 12]]}
    new_dictionar = {'Apartamentul 1': [['lumina', 134]]}
    stergere_cheltuiala_specifica('apa', dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134], ['apa', 12]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]]}
    new_dictionar = {'Apartamentul 1': [
        ['lumina', 134]], 'Apartamentul 4': [['lumina', 150]]}
    stergere_cheltuiala_specifica('apa', dictionar)
    assert dictionar == new_dictionar

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    new_dictionar = {'Apartamentul 1': [['lumina', 134]], 'Apartamentul 4': [
        ['lumina', 150]], 'Apartamentul 3': []}
    stergere_cheltuiala_specifica('apa', dictionar)
    assert dictionar == new_dictionar
    try:
        stergere_cheltuiala_specifica(asd, dictionar)
        stergere_cheltuiala_specifica('Apartametnul 1', dictionar)
        stergere_cheltuiala_specifica('af', dictionar)
        stergere_cheltuiala_specifica(asd, 3)
        assert False
    except:
        assert True


def test_suma_tot_cheltuiala():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    assert suma_tot_cheltuiala('apa', dictionar) == 459

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ], 'Apartamentul 3': [['apa', 15]]}
    assert suma_tot_cheltuiala('apa', dictionar) == 27

    dictionar = {'Apartamentul 1':  [[
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ], 'Apartamentul 3': [['apa', 15]]}
    assert suma_tot_cheltuiala('apa', dictionar) == 15

    dictionar = {'Apartamentul 1':  [[
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ], 'Apartamentul 3': []}
    assert suma_tot_cheltuiala('apa', dictionar) == 0


def test_suma_cheltuieli_apartament():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    assert suma_cheltuieli_apartament('Apartamentul 1', dictionar) == 146

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134], ['gaz', 1]]}
    assert suma_cheltuieli_apartament('Apartamentul 1', dictionar) == 147

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    assert suma_cheltuieli_apartament('Apartamentul 4', dictionar) == 582
    try:
        dictionar = {}
        assert suma_cheltuieli_apartament('', dictionar) == ''
        assert suma_cheltuieli_apartament('Apartamentul 1', dictionar) == ''
        assert False
    except Exception:
        assert True


def test_cheltuieli_mai_mici():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_mai_mici(1, dictionar) == [12, 134]

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_mai_mici(14, dictionar) == [134]

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_mai_mici(140, dictionar) == []

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 432], ['apa', 150]], 'Apartamentul 3': [['apa', 15]]}
    assert cheltuieli_mai_mici(140, dictionar) == [432, 150]
    try:
        cheltuieli_mai_mici('', dictionar)
        cheltuieli_mai_mici('', diction)
        cheltuieli_mai_mici('sadasad', dictionar)
        assert False
    except:
        assert True


def test_eliminare_cheltuieli():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 432], ['apa', 150]], 'Apartamentul 3': [['apa', 15]]}
    assert eliminare_cheltuieli('apa', dictionar) == ['lumina', 'lumina']

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 432], ['apa', 150]], 'Apartamentul 3': [['apa', 15]]}
    assert eliminare_cheltuieli('lumina', dictionar) == ['apa', 'apa', 'apa']

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134], ['gaz', 12]], 'Apartamentul 4': [['lumina', 432], ['apa', 150]], 'Apartamentul 3': [['apa', 15]]}
    assert eliminare_cheltuieli('lumina', dictionar) == [
        'apa', 'gaz', 'apa', 'apa']

    dictionar = {'Apartamentul 1': [['lumina', 12], [
        'lumina', 134], ['lumina', 12]], 'Apartamentul 4': [['lumina', 432], ['lumina', 150]], 'Apartamentul 3': [['lumina', 15]]}
    assert eliminare_cheltuieli('lumina', dictionar) == []


def test_cheltuieli_mai_mari():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_mai_mari(1, dictionar) == [
        'Apartamentul 1', 'Apartamentul 1']

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_mai_mari(14, dictionar) == ['Apartamentul 1']

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_mai_mari(140, dictionar) == []

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 432], ['apa', 150]], 'Apartamentul 3': [['apa', 15]]}
    assert cheltuieli_mai_mari(140, dictionar) == [
        'Apartamentul 4', 'Apartamentul 4']
    try:
        cheltuieli_mai_mari('', dictionar)
        cheltuieli_mai_mari('', diction)
        cheltuieli_mai_mari('sadasad', dictionar)
        assert False
    except:
        assert True


def test_cheltuieli_de_acelasi_tip():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_de_acelasi_tip('apa', dictionar) == [12]

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert cheltuieli_de_acelasi_tip('lumina', dictionar) == [134]

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 432], ['apa', 150]], 'Apartamentul 3': [['apa', 15]]}
    assert cheltuieli_de_acelasi_tip('apa', dictionar) == [12, 150, 15]
    try:
        cheltuieli_de_acelasi_tip('', dictionar)
        cheltuieli_de_acelasi_tip('', diction)
        cheltuieli_de_acelasi_tip('sadasad', dictionar)
        assert False
    except:
        assert True


def test_cheltuieli_inainte_de_zi():
    dictionar = {'Apartamentul 1': [['apa', 12, 3], [
        'lumina', 134, 24]]}
    assert cheltuieli_inainte_de_zi(1, 20, dictionar) == ['Apartamentul 1', 12]

    dictionar = {'Apartamentul 1': [['apa', 12, 2], [
        'lumina', 134, 1]]}
    assert cheltuieli_inainte_de_zi(10, 25, dictionar) == [
        'Apartamentul 1', 12, 'Apartamentul 1', 134]

    dictionar = {'Apartamentul 1': [['apa', 12, 12], [
        'lumina', 134, 11]]}
    assert cheltuieli_inainte_de_zi(140, 2, dictionar) == []

    dictionar = {'Apartamentul 1': [['apa', 12, 1], [
        'lumina', 134, 1]], 'Apartamentul 4': [['lumina', 432, 2], ['apa', 150, 2]], 'Apartamentul 3': [['apa', 15, 3]]}
    assert cheltuieli_inainte_de_zi(1, 25, dictionar) == [
        'Apartamentul 1', 12, 'Apartamentul 1', 134, 'Apartamentul 4', 432, 'Apartamentul 4', 150, 'Apartamentul 3', 15]
    try:
        cheltuieli_inainte_de_zi('', 1, dictionar)
        cheltuieli_inainte_de_zi('', '', diction)
        cheltuieli_inainte_de_zi('sadasad', 12, dictionar)
        assert False
    except:
        assert True


def test_sortare_apartamente():
    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    assert sortare_apartamente('apa', dictionar) == [
        'Apartamentul 1', 'Apartamentul 3', 'Apartamentul 4']

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]], 'Apartamentul 4': [['lumina', 150], ['apa', 432]], 'Apartamentul 3': [['apa', 15]]}
    assert sortare_apartamente('gaz', dictionar) == []

    dictionar = {'Apartamentul 1': [['apa', 12], [
        'lumina', 134]]}
    assert sortare_apartamente('apa', dictionar) == ['Apartamentul 1']

    try:
        sortare_apartamente('', dictionar)
        sortare_apartamente('', diction)
        sortare_apartamente('sadasad', dictionar)
        assert False
    except:
        assert True


def test_undo():
    global apartamente
    new_dict = {}
    adaugare_apartament(1, apartamente)
    add_to_stack("Apartamentul " + str(1))
    create_stiva_adaugare()
    s_pop()
    apartamente.clear()
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
    assert (apartamente == new_dict)

    new_dict = {'Apartamentul 1': []}
    curatare_stack()
    adaugare_apartament(1, apartamente)
    add_to_stack("Apartamentul " + str(1))
    create_stiva_adaugare()

    curatare_stack()
    adaugare_apartament(2, apartamente)
    add_to_stack("Apartamentul " + str(2))
    create_stiva_adaugare()

    s_pop()
    apartamente.clear()
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
    assert (apartamente == new_dict)

    new_dict = {'Apartamentul 1': []}
    curatare_stack()
    adaugare_cheltuiala('Apartamentul 1', 'apa', 12, 1, apartamente)
    add_to_stack('Apartamentul 1')
    add_to_stack('apa')
    add_to_stack(12)
    add_to_stack(1)
    create_stiva_adaugare_chl()
    s_pop()
    apartamente.clear()

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
    assert (apartamente == new_dict)

    new_dict = {}
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

    new_dict = {'Apartamentul 1': []}
    curatare_stack()
    modificare_cheltuiala('Apartamentul 1', 'apa', 1, apartamente)
    add_to_stack('Apartamentul 1')
    add_to_stack('apa')
    add_to_stack(1)
    create_stiva_modificare()
    s_pop()
    apartamente.clear()
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
    assert (apartamente == new_dict)


def run_all_test():
    test_adaugare_apartament()
    test_adaugare_cheltuiala()
    test_stergere_cheltuiala()
    test_modificare_cheltuiala()
    test_stergeri_consecutive()
    test_stergere_cheltuiala_specifica()
    test_suma_tot_cheltuiala()
    test_sortare_apartamente()
    test_suma_cheltuieli_apartament()
    test_cheltuieli_mai_mici()
    test_eliminare_cheltuieli()
    test_cheltuieli_mai_mari()
    test_cheltuieli_de_acelasi_tip()
    test_cheltuieli_inainte_de_zi()
    test_undo()
