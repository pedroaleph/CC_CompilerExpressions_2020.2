import analisador_sintatico.analisador_preditivo as asp
import analisador_sintatico.analisador_precedencia_fraca as apf
import analisador_sintatico.arvore_sintatica as arsp
import analisador_sintatico.as_apf as arpf
import string
import tkinter.messagebox as ms
operadores = ['+', '-', '*', '/', '%', '(', ')']
#tabela de equivalencia de proridade de operadores
# serve para substituir na gramatica G
E = {'+': '+', '-': '+', '*': '*', '/': '*', '%': '*', '=': '=', '(': '(', ')': ')'}
# lista para expressao
le = []
V = []
def analise_sintatica(linhas, dados):
    le = []
    expressoes = linhas
    cont = 0
    for e in expressoes:
        e.append(cont)
        cont += 1
    #print(expressoes)
    for x in expressoes:
        n = 0
        s = []
        for y in x:
            if type(y) is str: 
                if (x[n + 1] not in operadores) or (type(x[n+1]) is int):
                    #print(y,'1')
                    s.append(y)
                elif (y ==  '=') or y.isnumeric():
                        #print(y, '2')
                        s.append(y)
                elif (x[n+1] in operadores) and (s[-1] != '<'):
                    #print(y, '3')
                    s.append("<")
                    v  = []
                    if(x[n-1] == '('):
                        v.append('(')
                    v.append(y)
                    m = n + 1
                    while type(x[m]) is str:
                        v.append(x.pop(m))
                    #print(v,'4')
                    le.append(v) 
                n += 1
        le.append(s)
    #print(le)
    dados.append(le)
    #print(s)
    V = []
    for l in le:
        p = ""
        for c in l:
            #V.append(l)
            if (c != '=') and (c not in operadores):
                if (l[1] == '=') and (c != '<'):
                    p += 'i'
                else:
                    if (c == '(') or (c == ')'):
                        p += c
                    else:
                        p += 'v'
            else:
                p += E[c]
        V.append(p)

    #print(V)

    #print(le)
    # lista para a arvore
    A = []
    for a in V:
        if a[0] == 'i':
            if (asp.automatoM(a, asp.gramatica_A)):
                a = []
                a = asp.arv
                a = arsp.arvore_sintatica(a)
                a = arsp.ar_simp(a)
                A.append(a)
            else:
                ms.showerror('ERRO!', 'sentenca invalida na gramatica de atribuicoes')
                return False
        elif (a[0] == 'v') or (a[0] == '('):
            if(apf.automatoM(a, apf.gramatica_G)):
                a = []
                a = apf.arv
                a = arpf.arvore_sintatica(a)
                a = arpf.simplifica(a)
                A.append(a)
            else:
                ms.showerror('ERRO!', 'sentenca invalida na gramatica de expressoes')
                return False
    V = A
    print(V)
    dados.append(V)
    return True

#print(s)

def codigo_intermediario(dados):
    le = dados[0]
    V = dados[1]
        #print(le, 'le')
        #print(V, 'V')#colocando as variaveis corretas
    def correcao(a):
        #print(a)
        #print(s)
        if s != []:
            if len(a[1]) > 1:
                correcao(a[1])
            else:
                #print('s',s)
                a[1] = s.pop()
                #print(s)
            #print( 's1',s)
            a[0] = s.pop()
            #print(a)
            #print(s)
            if len(a[2]) > 1:
                #print('s2',s)
                correcao(a[2])
            else:
                #print('s3',s)
                a[2] = s.pop()
        #print('s4',s)
        return a

    def escrevendo(a):
        #print(a)
        if type(a[1]) != str:
            a[1] = escrevendo(a[1])
        if type(a[2]) != str:
            a[2] = escrevendo(a[2])
        temp = []
        if a[0] == '=':
            o = a[2]
            if o == '<':
                #print(str(t[0]))
                #o = 't' + str(t[0] - 1)
                list_in[-1][-1][0] = a[1]
                return a[1]
            #m = " :=" + " " + o + " ;\n"
            temp.append(a[1])
            temp.append(a[0])
            temp.append(o)
            cod_in.append(temp)
        else:
            te = []
            o = ["t" + str(t[0])]
            #m = " := " + a[1][0] + " " + a[0][0] + " " + a[2][0] + " ;\n"
            t[0] += 1
            te.append(a[1][0])
            te.append(a[0][0])
            te.append(a[2][0])

            temp.append(o[0])
            temp.append(te)

            cod_in.append(temp)
            return o
        return a[1]
    # para criar variavel temporaria
    t = [0]
    # verificando expressoes iguais

    def is_equal(cod_in):

        for c in cod_in:
            #print (c)
            igual = c
            for cod in cod_in:
                if cod != igual:
                    if cod[1] == igual[1]:
                        for con in cod_in:
                            if con[1][0] == cod[0]:
                                con[1][0] = igual[0]
                            elif con[1][2] == cod[0]:
                                con[1][2] = igual[0]
                        cod_in.pop(cod_in.index(cod))
            
    #adapatando para o arquivo saida
    def e_saida(cod_in):
        temp = []
        m = ""
        for e in cod_in:
            #print(e)
            if e[1] == '=':
                #print(e)
                m = e[0] + " := " + e[2] + " ; \n"
            else:
                m = e[0] + " := " + e[1][0] + " " + e[1][1] + " " + e[1][2] + " ; \n"
            temp.append(m)
        #print(temp)
        cod_in.clear()
        cod_in.append(temp)

    n = 0
    for a in V:
        s = le[n][::-1]
        print(s)
        while '(' in s:
            s.pop(s.index('('))
        while ')' in s:
            s.pop(s.index(')'))
        #print(s)
        a = correcao(a)
        n += 1

    print(V)
    list_in = []
    for a in V:
        cod_in = []
        a = escrevendo(a)
        #print(cod_in)
        if cod_in != []:
            if len(cod_in[0]) == 2:
                is_equal(cod_in)
                #print(cod_in)
            list_in.append(cod_in)

    for cod_in in list_in:
        e_saida(cod_in)

    print(list_in)

    # arquivo de saida com a espressao intermediaria
    saida = open('codigo_intermediario.txt', 'w')
    for l in list_in:
        saida.writelines(l[0])
        #saida.write('\n')
    saida.close()