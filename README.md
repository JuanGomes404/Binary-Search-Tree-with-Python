# Lista de exercícios

## 1 Uma árvore é uma estrutura tipicamente recursiva. Nós vimos um algoritmo iterativo para realizar busca. Porque não utilizar um algoritmo recursivo para a busca em uma árvore binária de busca?
Para algoritmos de busca, é mais eficiente utilizar soluçoes iterativas pois a complexidade de espaço (memória total ocupada)
será menor.

## 2 Elabore um algoritmo recursivo para efetuar uma busca em uma árvore binária de busca pressupondo as estruturas de dados do exemplo anterior.
Verificar métodos "search" e "searchRecursively" no arquivo "binarcy_search_tree.py".

## 3 Existe alguma razão para evitarmos algoritmos de busca em árvore recursivos (memória, complexidade, etc)? Justifique.
Sim, pois como já foi dito na primeira questao, a total de memória consumida nos algoritmo recursivos é maior do que nos algoritmos iterativos, fazendo com que esses sejam mais eficientes.

## 4 O algoritmo recursivo de inserção em árvore binária de busca apresentado é bastante simples e reflete bem a estrutura da própria árvore. Não será possível também realizar a função deste algoritmo com um algoritmo iterativo? Crie um algoritmo iterativo para a inserção simples em uma árvore binária de busca.
Sim, é possivel utilizar um algoritmo iterativo.
Verificar método "insertIteratively" no arquivo "binary_search_tree.py".

## 5 - Anulada

## 6 Faça um resumo de uma página + exemplos de código de árvore binária de busca, AVL e Rubro-negras.
As estruturas de dados baseadas em árvore organizam de um modo geral, seus elementos de uma forma hierárquica, na qual existe um elemento que fica no topo da árvore, chamado de raiz e existem os elementos subordinados a ele, que são chamados de nós filhos. Assim, há vários tipos de árvores em que cada uma possui a sua própria forma de organizar seus nós. Nesse sentido, alguns tipos são: Árvore binária de busca; Árvore AVL e Árvore Rubro-negra.

As Árvores Binárias de Busca são uma estrutura de dados em que todos os nós filhos da subárvore esquerda possuem um valor numérico inferior ao nó raiz, enquanto todos os nós filhos da subárvore direita possuem um valor superior a origem. Dessa forma, esse tipo de árvore é dinâmica, ou melhor, ao inserir ou excluir um determinado nó, os nós restantes se organizam a fim de cumprir a regra principal. 

Exemplo de Árvore Binária de Busca :

struct node {
   int data;
   struct node *leftChild;
   struct node *rightChild;
};
struct node* search(int data){
   struct node *current = root;
   printf("Elementos visitados: ");
	
   while(current->data != data){
	
      if(current != NULL) {
         printf("%d ",current->data);
			
         //vá para a subárvore da esquerda
         if(current->data > data){
            current = current->leftChild;
         }//senão, vá para a subárvore da direita
         else {                
            current = current->rightChild;
         }
			
         //não encontrado
         if(current == NULL){
            return NULL;
         }
      }			
   }
   return current;
}



Por sua vez , as árvores AVL são uma árvore na qual as alturas das subárvores esquerda e direita de cada nó diferem no máximo por uma unidade. Neste seguimento, podemos dizer que são árvores altamente balanceadas, isto é, a cada inserção e/ou exclusão, procura-se executar sempre uma rotina de balanceamento. 
Assim, se o fator de balanceamento de qualquer nó ficar menor do que -1 ou maior do que 1, então a árvore tem que ser balanceada, por meio das rotações simples ou rotações duplas.

Exemplo de Árvore AVL:

typedef struct aux {
	TIPOCHAVE chave;
	struct aux *esq;
	struct aux *dir;
	int bal; // fator de balanceamento (0, -1 ou +1) => alt. direita - alt. esquerda
} NO, *PONT;

/* cria um novo (aloca memória e preenche valores) no com chave=ch e retorna 
       seu endereço */
PONT criarNovoNo(TIPOCHAVE ch){
	PONT novoNo = (PONT)malloc(sizeof(NO));
	novoNo->esq = NULL;
	novoNo->dir = NULL;
	novoNo->chave = ch;
	novoNo->bal = 0;
	return novoNo;
}
/* Exibe arvore Em Ordem         */
void exibirArvoreEmOrdem(PONT raiz){
	if (raiz == NULL) return;
	exibirArvoreEmOrdem(raiz->esq);
	printf("%i ",raiz->chave);
	exibirArvoreEmOrdem(raiz->dir);
}















Por fim, as árvores Rubro Negras foram inventadas por Bayer sob o nome “Árvores Binárias Simétricas” em 1972, 10 anos depois das árvores AVL. Nesse sentido, esse tipo de árvore possui a mesma finalidade do tipo anterior, mas o balanceamento é feito por meio de um bit extra em cada nó que determina se esta é "vermelha" ou "preta" dentro do conjunto de regras que rege a árvore. 
Dessa maneira, não é necessário fazer um rebalanceamento em toda árvore a cada inserção ou exclusão, mas somente nos nós que foram afetados pela tal operação, tornando esse tipo de árvore, geralmente mais eficiente que as demais. 

Exemplo de Árvore Rubro Negra:

private class Node {
         Key     key;
         Value   val;
         Node    left, right;
         int     N;             // número de nós nesta subárvore
         boolean color;         // cor do link que aponta para este nó
   
         Node(Key key, Value val, int N, boolean color) {
            this.key   = key;
            this.val   = val;
            this.N     = N;
            this.color = color;
         }
      }

      private boolean isRed(Node x) {
         if (x == null) return false;
         return x.color == RED;
      } 

