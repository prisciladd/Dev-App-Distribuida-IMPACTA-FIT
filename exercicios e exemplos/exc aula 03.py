#listas:

a= [1,2,3]
print('Lista a', a)
b= [4,5,6]
print('Lista b', b)
c=a+b
print('Concatenou a + b:',c)


d= a*3
print('Multiplicou a 3 vezes:',d)



#tuplas:

lista1=list(range(5))
print('Criou lista sozinho com range 5',lista1)
print('Mostra do início até posição 3', lista1 [:3])

lista2=list(range(5,50,4)) #pula de 4 em 4
print('Criou lista sozinho com range começando em 5, até 50, pulando de 4 em 4',lista2)

print ('Mostra tamanho da lista',len(lista2))
print ('Mostra menor valor da lista',min(lista2))
print ('Mostra maior valor da lista',max(lista2))

#dicionario:

dic={}
dic['jose']=10
dic['maria']=220

dic[12345678901]= 'Alex', 23, 27345897
dic[63745678902]= 'João', 33, 27314567
dic[79845678903]= 'Josefa', 15, 27324569

print('mostra dicionário criado (chave: valor):',dic)

'''
print('mostra todas as chaves do dicionário' ,dic_keys())
print('mostra todos os valores do dicionário' ,dic_values())
'''