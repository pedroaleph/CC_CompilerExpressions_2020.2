'''
    O algoritmo le um vetor que tem salvo as producoes percorridas pela sentenca.
Iniciando pelo sentecial, ele o salva em um nodo e expande para a proxima producao,
assim, empilhando a proxima proxima posicao do vetor, ate que encontre um simbolo terminal, 
desempilhando e retornando para o nodo anterior. Dessa forma o algoritmo garante que 
as folhas sejam conectadas corretamente na arvore, assim como os nodos internos.

A arvore eh salva como lista, onde em cada nodo a primeira posicao contem um simbolo, e a
segunda posicao contem as producoes que este simbolo gera(nodos filhos).
'''
terminais = ['+', '*', '(', ')', 'v', '&', '=', 'i']
'''a = ['E', 'MF', 'PN', 'v', '&', '+MF', 'PN', 'v', '&', '&']'''
'''a = ['E', 'MF', 'PN', '(E)', 'MF', 'PN', 'v', '&', '&', '&', '&']'''
def arvore_sintatica(a):
    p = []
    q = [0]
    def add_nodo(n):
        nodo = []
        nodo.append(n)
        if n not in terminais:
            q[0] = q[0] + 1
            p.append(a[q[0]])
            for i in p[-1]:
                nodo.append(add_nodo(i[0]))
        else:
            p.pop()
        return nodo
    A = []
    p.append(a[q[0]])
    A.append(add_nodo(a[q[0]]))
    #print(A[0])
    return A[0]
    
def simplifica(a):
    #print(a)
    #if  len(a) == 2:
    if a[1][0] == '&':
        return '&'
    #else:
    #if a[1][0] == '(':
     #       return simplifica(a[2])
    #elif a[1][0] in terminais:
    #a = a[::-1]
    #a.pop()
    #a = a[::-1]
    #print(a)
    if len(a) == 2:
        a[1] = simplifica(a[1])
    else:
        a[2] = simplifica(a[2])
        if(a[2]) == '&':
            a.pop()
        else:
            if a[2][0] == 'B':
                t = a.pop()
                t.pop(0)
                a.extend(t)

    return a
    
def ar_sim(a):
    #print(a)
    #if a[1][0] in terminais:
     #   return a[1][0]
    #else:
    if a[0] not in terminais:
        if len(a) > 2:
            t = a[::-1]
            t.pop()
            a = []
            a.append(t[1][0])
            a.append(t[2][0])
            a.append(ar_sim(t[0]))
        else:
            a = ar_sim(a[1])
    else:
        return a[0]
    return a
def ar_simp(a):
    a = simplifica(a)
    #print(a)
    a = ar_sim(a)
    #print(a)
    return a
