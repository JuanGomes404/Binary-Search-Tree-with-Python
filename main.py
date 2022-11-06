class No:

    # Constructor to create a new node
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


# A utility function to do inorder traversal of BST
def preOrdem(raiz):
    if raiz:
        print(raiz.chave)
        preOrdem(raiz.esq)
        preOrdem(raiz.dir)


# A utility function to insert a
# new node with given key in BST
def inserir(no, chave):
    # If the tree is empty, return a new node
    if no is None:
        return No(chave)

    # Otherwise recur down the tree
    if chave < no.chave:
        no.esq = inserir(no.esq, chave)
    else:
        no.dir = inserir(no.dir, chave)

    # return the (unchanged) node pointer
    return no


# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def noMenorValor(no):
    atual = no

    # loop down to find the leftmost leaf
    while atual.esq is not None:
        atual = atual.esq

    return atual


# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deletarNo(raiz, chave):
    # Base Case
    if raiz is None:
        return raiz

    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if chave < raiz.chave:
        raiz.esq = deletarNo(raiz.esq, chave)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif (chave > raiz.chave):
        raiz.dir = deletarNo(raiz.dir, chave)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if raiz.esq is None:
            temp = raiz.dir
            raiz = None
            return temp

        elif raiz.dir is None:
            temp = raiz.esq
            raiz = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = noMenorValor(raiz.dir)

        # Copy the inorder successor's
        # content to this node
        raiz.chave = temp.chave

        # Delete the inorder successor
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
