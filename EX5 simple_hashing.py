# -*- coding: utf-8 -*- ORDENAÇÃO DE UMA LISTA:  
m = 5
#Preenchendo a tabela com elementos vazios 
tabela = [None for i in range (m)]

# Rode a tabela por todas as posições
for i in range (m):
    n = int(input("Digite um N:"))
    pos = n % m
    #Se não tem nada na posição
    if tabela[pos] is None:
        tabela[pos] = n
    else:
        pos += 1 #incremento
        
        #Caso a ultima posicao esteja ocupada volte ao inicio
        if pos > m - 1:
             pos = 0
        #Enquanto não encontrar uma posição vazia continue procurando    
        while tabela[pos] is not None:
            pos += 1
            #Caso a ultima posicao esteja ocupada volte ao inicio
            if pos > m - 1:
                pos = 0
        else:
        # Se achar coloca o valor lá
            tabela[pos] = n

print (tabela)