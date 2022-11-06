class No:

    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


def preOrdem(raiz):
    if raiz:
        print(raiz.chave)
        preOrdem(raiz.esq)
        preOrdem(raiz.dir)


def inserir(no, chave):
    if no is None:
        return No(chave)

    if chave < no.chave:
        no.esq = inserir(no.esq, chave)
    else:
        no.dir = inserir(no.dir, chave)

    return no



def noMenorValor(no):
    atual = no
    while atual.esq is not None:
        atual = atual.esq

    return atual



def deletarNo(raiz, chave):
    # Base Case
    if raiz is None:
        return raiz

    if chave < raiz.chave:
        raiz.esq = deletarNo(raiz.esq, chave)

    elif (chave > raiz.chave):
        raiz.dir = deletarNo(raiz.dir, chave)

    else:

        if raiz.esq is None:
            temp = raiz.dir
            raiz = None
            return temp

        elif raiz.dir is None:
            temp = raiz.esq
            raiz = None
            return temp

        temp = noMenorValor(raiz.dir)

        raiz.chave = temp.chave

        raiz.dir = deletarNo(raiz.dir, temp.chave)

    return raiz


def main():
    bst = No(8)
    bst = inserir(bst, 3)
    bst = inserir(bst, 1)
    bst = inserir(bst, 5)
    bst = inserir(bst, 6)
    bst = inserir(bst, 7)
    bst = inserir(bst, 11)
    bst = inserir(bst, 9)
    bst = inserir(bst, 10)
    bst = inserir(bst, 14)
    bst = inserir(bst, 12)
    bst = inserir(bst, 15)
    bst = inserir(bst, 13)
    print("Árvore inicial: ")
    preOrdem(bst)
    print('\n')
    print("Árvore sem o 3:")
    deletarNo(bst,3)
    preOrdem(bst)
    print('\n')
    print('Árvore sem o 12:')
    deletarNo(bst,12)
    preOrdem(bst)

main()
