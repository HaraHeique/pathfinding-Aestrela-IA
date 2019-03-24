# -*- coding: utf-8 -*-

"""
    Responsável por lidar com a entrada de dados do usuário especificamente para o pathfinding
"""

def pontoInicial(mtzMap: list) -> tuple :
    while (True) :
        ptoInput: str = input("\nInsira o ponto inicial no formato x,y: ")
        pontoInicial: tuple = __getPontoSelecionado(mtzMap, ptoInput)

        if (pontoInicial is not None) :
            return pontoInicial


def pontoFinal(mtzMap: list) -> tuple :
    while (True) :
        ptoInput: str = input("\nInsira o ponto final no formato x,y: ")
        pontoFinal: tuple = __getPontoSelecionado(mtzMap, ptoInput)

        if (pontoFinal is not None) :
            return pontoFinal


def __getPontoSelecionado(mtzMap: list, ptoInput: str) -> tuple :
    if (not __isPtoInputValid(ptoInput)) :
        print("O ponto não segue o formato(x,y) desejado.")
        return None
    
    ptoInput = ptoInput.split(',')
    ptoSelecionado: tuple = (int(ptoInput[0]), int(ptoInput[1]))

    if (not __isValidPto(mtzMap, ptoSelecionado)) :
        print("O ponto inserido viola os limites da matriz.")
        return None
    
    if (not __isObstaculo(mtzMap, ptoSelecionado)) :
        print("O ponto selecionado é um obstáculo. Favor selecionar os de valor 0")
        return None

    return ptoSelecionado


# Checa se o ponto no formato (x, y) inserido pelo usuário é válido
def __isPtoInputValid(ptoInput: str) -> bool :
    ptoSplit: list = ptoInput.split(',')
    
    if (list.__len__(ptoSplit) != 2 or not ptoSplit[0].replace('-', '').isdigit() or not ptoSplit[1].replace('-','').isdigit()) :
        return False
    
    return True


# Checa se o ponto inserido é um obstáculo no mapa
def __isObstaculo(mtzMap: list, ptoSelecionado: tuple) -> bool :
    
    # Diferente de zero é porque certamente é um obstáculo
    if (mtzMap[ptoSelecionado[0]][ptoSelecionado[1]] != 0) :
       return False
    
    return True


# Checa se o ponto inserido viola os limites da matriz
def __isValidPto(mtzMap: list, ptoSelecionado: tuple) -> bool :
    linMax: int = list.__len__(mtzMap)

    if (linMax == 0 or ptoSelecionado[0] < 0 or ptoSelecionado[0] > linMax-1) :
        return False
    
    colMax: int = list.__len__(mtzMap[0])

    if (ptoSelecionado[1] < 0 or ptoSelecionado[1] > colMax-1) :
        return False
    
    return True

# Para testes
if __name__ == '__main__':
    pontoInicial([[5, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])