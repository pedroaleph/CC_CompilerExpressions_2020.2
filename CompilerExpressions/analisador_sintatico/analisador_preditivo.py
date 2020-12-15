'''
Analisador Sintatico para gramatica de atribuicoes
    A gramatica (A'') faz um id (esta como i) receber algo, que pode ser outro 
 id (i = i), ou uma expressao complementando a gramatica G (i = v). 
 A gramatica tambem aceita atribuicoes em sequencia, neste caso, a expressao, se 
 houver, deve estar somente na ultima atribuicao (ex: i=i=v)

 ela foi implentada de forma que ja seja possivel ler suas producoes e tabela sintatica
'''
gramatica_A = {
    'terminal' : {'i': 0, '=': 1, 'v': 2, '$': 3},
    'simbolos' : {'A': 0, 'B': 1, 'I': 2, 'J': 3},
    'producao' : {1: "Bi", 2: "I=", 3: "A", 4: "Jv", 5: "&", 6: "&"},
    'sentencial' : 'A',
    'M' : [[1, 0, 0, 0], [0, 2, 0, 5], [3, 0, 4, 0], [0, 0 , 0, 6]]
}
'''gramatica G'''
gramatica_G = {
    'terminal': {'+': 0, '*': 1, '(': 2, ')': 3, 'v': 4, '$': 5},
    'simbolos' : {'E': 0, 'F': 1, 'M':2, 'N': 3, 'P': 4},
    'producao' : {1: "FM", 2: "FM+" ,3: "&", 4: "NP", 5: "NP*", 6: "&", 7: ")E(", 8: "v"},
    'sentencial' : 'E',
    'M' : [[9,9,1,9,1, 9], [2,9,9,3,9,3], [9,9,4,9,4,9], [6,5,9,6,9,6], [9,9,7,9,8,9]]
    }
''''arvore sintatica'''
# import arvore_sintatica as ar
arv = []
# A = []
'''implementacao do slide 11'''
gramatica = {'G': gramatica_G, 'A' : gramatica_A}
def automatoM(s, g):
    if arv != []:
        arv.clear()
    s = s + '$'
    M = g['M']
    pilha  = []
    pilha.append('$')
    pilha.append(g['sentencial'])
    '''vetor para a arvore'''
    arv.append(pilha[-1])
    '''c e l inicialmente em nenhum dos casos'''
    c = -1
    l = -1
    #print(s)
    for i in s:
        '''procurando sentenca usando dicionario'''
        if i[0] in g['terminal'].keys():
            c = g['terminal'][i[0]]
        else:
            return False
        while True:
            if pilha[-1] in g['simbolos'].keys():
                l = g['simbolos'][pilha[-1]]
            else:
                return False
            '''producao conforme a tabela'''
            Nprod = M[l][c]
            prod = -1
            #print ("P",Nprod)
            if Nprod in g['producao'].keys():
                prod = g['producao'][Nprod]
            else:
                return False
            if prod[0]=='&':
                pilha.pop()
                arv.append('&')
            else:
                pilha.pop()
                for j in prod:
                    pilha.append(j[0])
                arv.append(prod[::-1])
            #print (pilha)
            if pilha[-1] == i[0]:
                if i[0] == '$':
                    return True
                else:
                    pilha.pop()
                    break

'''testando'''
'''print('G - gramatica de expressoes\nA - gramatica de atribucao\ndigite a gramatica:')
g = input()
print ("digite a sentenca:")
sentenca = input()
if automatoM(sentenca, gramatica['G']):
    print ("sentenca aceita")
    print(a)
    A = ar.arvore_sintatica(a)
    print(ar.ar_simp(A))
else:
    print ("sentenca nao aceita")
'''