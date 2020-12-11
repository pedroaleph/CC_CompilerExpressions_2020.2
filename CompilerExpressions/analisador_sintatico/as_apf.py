terminais = ['+', '*', '(', ')','v']
producao = {"M+E": 'E', "M" : 'E', "P*M": 'M', "P": 'M', ")E(": 'P', "v" : 'P'}
'''a = ['v', 'P', 'M', 'E', '+', 'v', 'P', 'M', '*', 'v', 'P', 'M', 'E']'''
'''a = ['(', 'v', 'P', 'M', 'E', ')', 'P', 'M', 'E']'''
def arvore_sintatica(a):
    '''inverte a lista 'a' para assim ir desempilhando quando uma producao eh encontrada'''
    a = a[::-1]
    '''lista para a arvore'''
    p = []
    while a != []:
        '''primeiro encontra um terminal'''
        if a[-1] in terminais:
            p.append(a.pop())
        else:
            '''caso os simbolos do topo de 'p' e 'a' se combinem em alguma producao,
            o simbolo do topo de 'p' eh desemplilhado e se torna filho do simbolo
            do topo de a, e este eh adicionado a 'p' '''
            q = ""
            '''para resolver os casos de ambiguidade, procura-se se o simbolo no topo de 'p'
            se combina com os proximos dois simbolos de 'p' em alguma producao,
             dando prioridade se for encontrado'''
            if len(p) > 2:
                r = p.copy()
                while len(q) < 3:
                    q = q + r[-1][0]
                    r.pop()
            '''caso ')' esteja no topo de 'p', o topo de 'a' sera sempre 'P',
            por isso nao eh necessario verificar se combinam'''
            if (p[-1][0] == ')') or (a[-1] == producao[p[-1][0]]):
                nodo = []
                nodo.append(a.pop())
                '''verificando se ha ambiguidade'''
                if q in producao.keys():
                    t = []
                    t.append(p.pop())
                    t.append(p.pop())
                    t.append(p.pop())
                    nodo.append(t[::-1])
                else:
                    nodo.append(p.pop())
                p.append(nodo)
    print (p[0])
    return p[0]

def simplifica(a):
    if a[1] in terminais:
        return a[1]
    else:
        if a[1][0] == '(':
            return simplifica(a[1][1])
        if len(a[1]) > 2:
            print(a)
            t = a[1]
            a = []
            a.append(t[1])
            a.append(simplifica(t[0]))
            a.append(simplifica(t[2]))
        else:
            a = simplifica(a[1])
    print(a)
    return a


    
