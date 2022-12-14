#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import sys

class Numeros:
    """
    Gera os numeros para cada letra do bingo.
    
    O bingo inicia em 1 até o numero 75, dividido em 5 colunas 
    B de 1 a 15, I de 16 a 30, N de 31 a 45, G de 46 a 60 e O de 61 a 75
    """
    def __init__(self):
        self.numeros = [[],[],[],[],[]]
        for x in range(0,5):
            for y in range(x*15+1,(x+1)*15+1):
                self.numeros[x].append(y)

class Cartela:
    """
    Gerencia as cartelas do bingo.
    
    Cria uma nova cartela gerada apartir de numeros aletorio preenchendo cada 
    coluna da cartela do bingo de acordo com a quantidade de numeros informadas
    nos parametros de inicialização da classe
    """                
    def __init__(self,num,chave,b=5,i=5,n=5,g=5,o=5):
        self.pedrasmarcadas = 0
        self.cartela = [[],[],[],[],[]]
        self.quantidade = [b,i,n,g,o]
        self.chave = chave
        for x in range(0,5):
            self.cartela[x] = random.sample(num.numeros[x],self.quantidade[x])
            self.cartela[x].sort()
            
    def __eq__(self,other):
        """
        Compara duas cartelas.
        """
        return(self.cartela == other.cartela)
    
    def __str__(self):
        """
        Texto com a chave da cartela.
        """
        return("Cartela %s" % (self.chave))
        
    def exibeCartela(self):
        """
        Imprime na saida padrão os numeros da cartela.
        """
        print(" = ", 3*5)
        print ("Cartela %s" % (self.chave))        
        print(" = ", 3*5)
        print ("%3s%3s%3s%3s%3s" % ("B","I","N","G","O"))
        for x in range(0,5):
            print ("%3d%3d%3d%3d%3d" % (self.cartela[0][x],self.cartela[1][x], \
            self.cartela[2][x],self.cartela[3][x],self.cartela[4][x]))
        print(" = ", 3*5)
    
    def existePedra(self,pedra):
        """
        Verifica a existencia da pedra na cartela.

        Identifica a qual coluna a pedra pertence em seguida verifica se nesta
        coluna existe a pedra,que é usada como retorno, ou uma lista vazia é
        retornada caso não exista a pedra na cartela
        """
        col = pedra / 15
        if pedra % 15 == 0:
            col = col - 1

#        retorno = []
#        for x in self.cartela[col]:
#            if pedra == x:
#                retorno = [x]
#        return(retorno) 

# O mesmo codigo pode ser escrito como abaixo:
        
        return([x for x in self.cartela[col] if pedra == x])

class Bingo: 
    def __init__(self):
        """
        Iniciando o bingo.
    
        É inicializado o vetor de cartelas, as pedras restantes (no inicio do
        bingo: todas as pedras são as restantes) e as pedras do bingo separadas
        por coluna 5 colunas B I N G O.
        """
        self.cartelas = []
        self.restantes = range(1,76)
        self.pedras = Numeros()
        
    def removeNumerodosrestantes(self,numero):
        """
        Remove um numero da lista de numeros restantes no bingo.
    
        Cada numero da lista de restantes é comparado com o numero a ser
        removido, apenas os restantes diferentes do numero a ser removido são
        inseridos na nova lista. Incrementa-se pedras marcadas nas cartelas que
        possuem o numero a ser removido.
        """
        self.restantes = filter(lambda arg:arg != numero,self.restantes)
        
        #Verificando quais cartelas possuem o numero removido para incrementar
        # o numero de pedras marcadas nas cartelas
        for cartela in self.cartelas:
            if cartela.existePedra(numero):
#                cartela.pedrasmarcadas = cartela.pedrasmarcadas + 1            
                cartela.pedrasmarcadas +=  1
    
    def adicionaCartela(self,cartela):
        """
        Adiciona uma nova cartela a lista de cartelas do Bingo.
        """
        self.cartelas.append(self.confereCartela(cartela))
#        self.cartelas.append(Cartela(self.pedras,chave))

    def confereCartela(self,comparar):
        """
        Compara se uma cartela exite idêntica na lista de cartelas do bingo.
        
        Retorna a cartela comparada caso não exista uma com os mesmos numeros na
        lista de cartelas do bingo e False caso ela exista na lista
        """
        for x in self.cartelas:
#               if x.cartela == comparar.cartela:
# Agora usando a implementação de igualdade __eq__ da classe Cartela
                if x == comparar:
                    comparar = self.confereCartela(Cartela(self.pedras,comparar.chave))
                    break                   
        return(comparar)

    def sorteaPedra(self):
        """
        Escolhe uma pedra entre as restantes no bingo.
        """
        return(random.choice(self.restantes))

def inicio():
    """
    iniciando o bingo.
    
    Simulação de utilização do aplicativo Bingo.
    """
    
    b = Bingo()

    #Criando Cartelas
    for x in range(0,100):
        b.adicionaCartela(Cartela(b.pedras,x+1))
        print(b.cartelas[x])
    #    b.cartelas[x].exibeCartela()

    #Demostração que cartelas repetidas não entram na lista de cartelas
    print(b.cartelas[0])
    #eu gostaria de ter tirado uma copia do objeto aqui mas nao sei como fazer
    #desta forma apenas uma copia do endereço do conteudo do objeto foi feita
    #ou seja a fala é exatamente a mesma primeira cartela
    falsa = b.cartelas[0]
    #quando altero a chave da falsa estou alterando a chave da primera tb
    falsa.chave = "Falsa"
    falsa.exibeCartela()
    b.adicionaCartela(falsa)
    #e isso a prova q uma mesma cartela (levando em cosideração os numeros) não
    #é adicionada duas vezes na lista de cartela do bingo
    b.cartelas[x+1].exibeCartela()
    #isso é a prova de que nao foi feito uma copia
    b.cartelas[0].exibeCartela()

    
    # simulando um bingo
    while b.restantes:
        pedrasorteada = b.sorteaPedra()
        print (pedrasorteada,
        b.removeNumerodosrestantes(pedrasorteada))
        for cartela in b.cartelas:
            if cartela.pedrasmarcadas == 25:
                print
                print ("BATEU")
                print ("Faltavam %d") % (len(b.restantes)) 
                print (b.restantes)
                cartela.exibeCartela()
                sys.exit()

#Executando o aplicativo se for chamado diretamente
if __name__ == '__main__':
    inicio()
