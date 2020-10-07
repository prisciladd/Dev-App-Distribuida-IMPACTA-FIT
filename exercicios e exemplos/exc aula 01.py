#1) Dada a lista L= [5, 7, 2, 9, 4,1, 3],escreva um programa que imprima
#as seguintes informações:

#a) tamanho da lista. 
#b) maior valor da lista. 
#c) menor valor da lista. 
#d) soma de todos os elementos da lista. 
#e) lista em ordem crescente. 
#f) lista em ordem decrescente.


lista=[5,7,2,9,4,1,3]

print('Tamanho da lista:', len(lista),
'Maior valor da lista:',max(lista),
'Menor valor da lista:', min(lista),
'Soma dos valores da lista:', sum(lista),
'Ordem crescente da lista:', lista.sort, 
'Ordem decrescente da lista:', lista.reverse)