import libraries.userInput as userInput
import libraries.utilities.matricesHandle as mtzHandle
import libraries.pathfindingHeuristic as heuristic
import os

def main(filesDir) :
    # Cria a matriz grid a partir de um arquivo
    mtzMap: list = mtzHandle.openMtzFromPathFile(filesDir + "map_default.txt")

    # Pega as informações dos pontos inicial e final inseridos pelo usuário
    mtzHandle.printar(mtzMap)
    pontoInicial: tuple = userInput.pontoInicial(mtzMap)
    pontoFinal: tuple = userInput.pontoFinal(mtzMap)

    # Cria a matriz de heurística baseado na matriz grid baseado no cálculo da distância de Manhatan
    mtzHeuristic: list = heuristic.matrizHeuristica(mtzMap, pontoFinal)
    mtzHandle.printar(mtzHeuristic)

    # Pega o melhor caminho traçado pelo algoritmo com base na matriz heurística
    caminhoTracado: list = heuristic.getCaminhoPercorrido(mtzMap, mtzHeuristic, pontoInicial, pontoFinal)
    print("\nCaminho Percorrido: {0}".format(caminhoTracado))

    return 0

if __name__ == '__main__':
    filesDir = os.path.dirname(os.path.realpath('__file__')) + "/src/files/"
    main(filesDir)