'''gramatica G em precedencia fraca'''
'''listas para a construcao da arvore sintatica'''
# import as_apf as ar
arv = []
# Arv = []
gramatica_G = {
    'producao' : {"M+E": 'E', "M" : 'E', "P*M": 'M', "P": 'M', ")E(": 'P', "v" : 'P'},
    'simbolo' : {'E': 0, 'M': 1, 'P': 2, '+': 3 , '*': 4, '(': 5, ')': 6, 'v': 7, '$': 8},
    'terminal' : {'+': 0 , '*': 1, '(': 2, ')': 3, 'v': 4, '$': 5},
    'nterminal' : ['E', 'M', 'P', ')'],
    'sentencial': 'E',
    'M' : [['D', 0, 0, 'D', 0, 0], ['R', 'D', 0, 'R', 0, 'R'], 
     ['R', 'R', 0, 'R', 0, 'R'], [0, 0, 'D', 0, 'D', 0],
      [0, 0, 'D', 0, 'D', 0], [0, 0, 'D', 0, 'D', 0],
       ['R', 'R', 0, 'R', 0, 'R'],  ['R', 'R', 0, 'R', 0, 'R'],
      [0, 0, 'D', 0, 'D', 0]]
}
def automatoM(s, g):
    s = s + '$'
    M = g['M']
    pilha  = []
    pilha.append('$')
    '''c e l inicialmente em nenhum dos casos'''
    c = -1
    l = -1
    '''invertendo a sentenca para assim remover o ultimo simbolo
     depois de ser analisado'''
    s = s[::-1]
    print(s)
    while True:
        '''procurando sentenca usando dicionario'''
        if s[-1] in g['terminal'].keys():
            pilha.append(s[-1])
            s = s[:-1]
            arv.append(pilha[-1])
        else:
            print(s[-1]," nao faz parte da gramatica")
            return False
        if s[-1] in g['terminal'].keys():
            c = g['terminal'][s[-1]]
        else:
            print(s[-1]," nao faz parte da gramatica")
            return False
        while True:
            l = g['simbolo'][pilha[-1]]
            '''producao conforme a tabela'''
            prod = M[l][c]
            if prod == 'R':
                print(pilha)
                '''para resolver a ambiguidade, verfica se os tres primeiros simbolos
                 no topo da pilha formam algum lado esquedo da producao, colocado os
                 no mesmo indice do topo da pilha caso seja encontrado, assim sendo priorizado'''
                if len(pilha) > 3:
                    if pilha[-1] in g['nterminal']:
                        r = pilha.copy()
                        q = ""
                        while len(q) < 3:
                            q = q + r.pop()
                        if q in g['producao'].keys():
                            r.append(q)
                            pilha = r
                        print(pilha)
                p = pilha.pop()
                pilha.append(g['producao'][p])
                arv.append(pilha[-1])
            else:
                if prod == 'D':
                    break
                else:
                    print("erro na producao da tabela sintatica")
                    return False
            if pilha[-1] == g['sentencial'] and s[-1] == '$':
                print(pilha)
                print (arv)
                return True
'''testando
print ("digite a sentenca:")
sentenca = input()
if automatoM(sentenca, gramatica_G):
    print ("sentenca aceita")
    Arv = ar.arvore_sintatica(arv)
    print(ar.simplifica(Arv))
else:
    print ("sentenca nao aceita")
'''