# -*- coding: utf-8 -*-

"""
    Lida com a lógica do caminho a ser do algoritmo pathfinding A* com base no cálculo
    da heurística
"""

# Retorna a matriz heurística baseado na matriz passada que é o mapa
def matrizHeuristica(mtz: list, pontoFinal: tuple) -> list:
	matEuri: list = []
	lin: int = len(mtz)
	col: int =  len(mtz[0]) if (lin > 0) else 0

	for i in range(lin):
		matEuri.append([])

		for j in range(col):
            # Caso seja diferente de zero é porque é um obstáculo logo seta um valor negativo
			if(mtz[i][j] != 0):
				matEuri[i].append(-1)
			else:
                # Faz o cálculo da distância de Manhattan do ponto corrente com o ponto final
				matEuri[i].append((abs(i-pontoFinal[0])+(abs((j-pontoFinal[1])))))
	
	return matEuri

# Pega a lista de caminhos baseado na matriz de heuristica e na matriz do mapa
def getCaminhoPercorrido(mtzMap: list, mtzHeuristica: list, ptoInicial: tuple, ptoFinal: tuple) -> list:
    
    if (ptoInicial == ptoFinal):
        return [ptoInicial]
    
    #CUSTO: int = 0 # Será o custo de percorrer para qualquer caminho
    ptoCurrent: tuple = ptoInicial
    found: bool = False
    pathTraced: list = [ptoInicial]
    
    while (not found):
        # Guarda o ponto anterior para que seja comparado com o novo ponto corrente/atual
        ptoAnteriorTraced = pathTraced[-2] if (len(pathTraced) > 1) else pathTraced[-1]
        ptoCurrentAntes = ptoCurrent
        ptoCurrent = __nextPonto(mtzHeuristica, ptoAnteriorTraced, ptoCurrent)

        if (ptoCurrent == ptoCurrentAntes):
            raise Exception("Não é possível sair do ponto {0}. Favor checar o código".format(ptoCurrent))
        
        # Adiciona o novo ponto ao caminho percorrido pelo algoritmo
        pathTraced.append(ptoCurrent)

        found = True if (ptoCurrent == ptoFinal) else False
    
    return pathTraced
        
# Pega a próxima célula que é adicionado na lista de caminho traçados
def __nextPonto(mtzHeuristica: list, ptoAnterior: tuple, ptoCurrent: tuple) -> tuple:
    
    LINMAX = len(mtzHeuristica)-1
    COLMAX = len(mtzHeuristica[0])-1 if (LINMAX > 0) else 0

    # As direções são respectivamente cima, baixo, esquerda, direita
    direcoes = [(ptoCurrent[0]-1, ptoCurrent[1]), 
                (ptoCurrent[0]+1, ptoCurrent[1]),
                (ptoCurrent[0], ptoCurrent[1]-1),
                (ptoCurrent[0], ptoCurrent[1]+1)]
    
    # Seta o valor como NULL inicialmente até que pegue o primeiro ponto que seja válido 
    menorCustoFuncaoHeuristica = None

    # Percorrendo pelas direções e checando qual delas será a selecionada como próximo caminho corrente
    for direcao in direcoes:
        # Checando se quebra os limites da matriz
        if (direcao[0] < 0 or direcao[0] > LINMAX or direcao[1] < 0 or direcao[1] > COLMAX):
            continue
        
        # Checa se o ponto da direção não é um obstáculo ou se já foi percorrido
        if (ptoAnterior == direcao or mtzHeuristica[direcao[0]][direcao[1]] < 0):
            continue
        
        # Caso a célula da matriz heurística na determinada direção seja menor do que o ponto corrente
        if (menorCustoFuncaoHeuristica == None or mtzHeuristica[direcao[0]][direcao[1]] < menorCustoFuncaoHeuristica):
            ptoCurrent = direcao
            menorCustoFuncaoHeuristica = mtzHeuristica[direcao[0]][direcao[1]]

    return ptoCurrent

# Desenha o mapa traçado passando como argumento uma lista de caminhos traçados
def drawMapTraced(mtzMap: list, caminhoTracado: list) -> None:

    if (len(mtzMap) == 0 or len(caminhoTracado) == 0):
        return

    for cell in caminhoTracado:
        mtzMap[cell[0]][cell[1]] = '*'
    
    # Mudando o símbolo do ponto final
    mtzMap[caminhoTracado[-1][0]][caminhoTracado[-1][1]] = 'F'

    # Mudando o símbolo do ponto inicial
    mtzMap[caminhoTracado[0][0]][caminhoTracado[0][1]] = 'I'

    return

if __name__ == '__main__':
    from utilities.matricesHandle import printarWithPadding

    mtz = [[0,1,0,0,0,0],
		   [0,1,0,0,0,0],
		   [0,1,0,0,0,0],
		   [0,1,0,0,0,0],
		   [0,0,0,0,1,0]]
    mtzEuri = matrizHeuristica(mtz, (4,5))
    caminhoPercorrido = getCaminhoPercorrido(mtz, mtzEuri, (0,0), (4,5))
    printarWithPadding(mtzEuri, 3)
    print("\nCaminho Percorrido: {0}".format(caminhoPercorrido))

    