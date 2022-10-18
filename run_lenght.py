import numpy as np


def run_lenght(bytes):
    aux = []
    count = 0
    iter = 0
    for i in bytes:
        iter += 1
        if i == 0:
            if iter == len(bytes):
                aux.append(i)
                aux.append(count + 1)
            else:
                count += 1
        else:
            if count == 0:
                aux.append(i)
            else:
                aux.append(0)
                aux.append(count)
                aux.append(i)
                count = 0
    return aux


def run_lenght_letters(bytes):
    llista = list(bytes)
    aux = []
    count = 0
    var = 0
    lletra = ''
    for i in llista:
        if lletra == '':
            lletra = i
            count += 1
        elif i != lletra:
            aux.append(lletra)
            aux.append(count)
            count = 1
            lletra = i
        else:
            count += 1
    aux.append(lletra)
    aux.append(count)
    return aux
