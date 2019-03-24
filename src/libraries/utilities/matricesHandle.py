# -*- coding: utf-8 -*-

"""
    Lidar com manipulação de matrizes
"""

# Printa no formato de matriz, porém ajusta o padding entre os pontos sozinho
def printar(mtz: list) -> None :
    for lines in mtz :
        print()
        for elem in lines :
            print("{:3d}".format(elem), end="")
    print('\n')

    return

# Printa no formato de matriz, porém ajusta o padding é passado como argumento
def printarWithPadding(mtz: list, padding: int) -> None :
    for lines in mtz :
        print()
        for elem in lines :
            print("%*d" %(padding, elem), end="")
    print('\n')

    return

# Cria a matriz baseado no caminho do arquivo passado como argumento
def openMtzFromPathFile(pathFile: str) -> list :
    mtz = []

    try:
        with open(pathFile, 'r') as f:
            for line in f:
                mtz.append([int(x) for x in line.split()])
    except Exception:
        raise

    return mtz