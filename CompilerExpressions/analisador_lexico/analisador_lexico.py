import re
import varredor

'''lista que armazenara caso todos os caractere sejam aceitos com seu respectivo automato'''
palavras = []
# alfabeto
alfabeto = {'a' : 0, 'b': 1}
def verifica(i):
    if re.findall("[_|a-z]", i):
        return 'a'
    elif re.findall("[0-9]", i):
        return 'b'
    return False
def automatov (L):
    '''matriz do automato de variáveis'''
    M = [[ 1, 1], [ -1, 1]] 
    e = 0 
    for i in L:
        l  = verifica(i)
        if l in alfabeto.keys():
            e = M[alfabeto[l]][e]
        else:
            return False
    '''Estado Final '''
    if e == 1:
        print ('reconhecido')
        '''
            palavras[0].append(L)
            palavras[1].append(1)
            '''
        return True
    else:
        return False
def  automato(L):
    if automatov(L):
        return True
    else:
        print ('nao reconhecido')
        return False


'''lista que recebera as palavras a serem a analisadas'''
caracteres = []
'''
caso usassemos o varredor, iriamos analisar somente os ID's que não são palavras reservas
mas so utilizaremos um arquivo simples para testar desse vez
lista = varredor.varredura()
for c in lista:
    if c[1] == 'ID':
        caracteres.append(c[0])
'''
'''lendo arquivo'''
arquivo = open ('arquivo.txt', 'r')
for linha in arquivo:
    linha = linha.split()
    caracteres.append(linha)
arquivo.close()

'''analisando os caracteres'''
for c in caracteres:
    print(c[0])
    automato(c[0])
    '''
    if automato(c[0]) == False:
        break
    '''


