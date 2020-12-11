import re
import string
import sys 
'''reconhecer variaveis declaradas'''
# tipos de variaveis
tipo = {'int': int, 'float': float, 'double': float, 'char': str, 'void': None}
sinais = ['+', '-', '*', '/', '%', '=']
# verifica se ha uma vairavel
def is_var(v):
    if type(v) is str:
        if re.findall("[_|a-z]", v[0]):
            return True
    return False

# linha de codigo
trechos = []
# arquivo para testar
# para armazenar ao numero da linha
n_line = 1
arquivo = open('semantico.txt', 'r')
for linha in arquivo:
    linha = linha.split()
    linha.append(n_line)
    trechos.append(linha)
    n_line -= - 1
arquivo.close()

print(trechos)

# lista que recebera as declaracoes
declaracoes = {}
# lista que que verififica inicio e termino de funcao
isFunc = []

for t in trechos:
    if t[0] in tipo.keys():
        # declaracao com atribuicao
        t[0] = tipo[t[0]]
        dt = []
        declaracoes[t[1]] = [t[0], t[-1], t[-1]]
        if t[2] == '=':
            dt = t
            dt.pop(0)
        elif len(t) > 4:
            isFunc.append(t[1])
            #print(isFunc[-1])
            n = 3
            while 1:
                #print(t[n])
                #print(trechos)
                if (t[n] in tipo) and (is_var(t[n+1])):
                    t[n] = tipo[t[n]]
                    declaracoes[t[n+1]] = [t[n], t[-1], t[-1]]
                    #print(declaracoes)
                    n+=2
                elif (t[n] == ','):
                        n+=1
                else:
                    break
        if dt != []:
            t = dt
        else:
            t.clear()
        
    elif len(t) == 2:  
        # print("entrou")
        if t[0] == '}':
            declaracoes[isFunc[-1]][2] = t[1]
            isFunc.pop()
            t.clear()       
        
res = list(filter(None, trechos))
trechos = res
print(trechos)
print(declaracoes)
# tratando declaracoes nas funcoes
r = list(declaracoes.keys())
b = r[::-1]
#print(r)
for f in b:
    i = declaracoes[f]
    if (i[1] != i[2]):
        #print(i)
        for g in b:
            j = declaracoes[g]
            if (j[1] == j[2]):
                #print(j)
                if (i[1] <= j[1]):
                    if i[2] > j[2] :
                        declaracoes[g][2] = i[2]
                #print( declaracoes[g])
                
print(declaracoes)
# analisando variaveis nas expressoes
for t in trechos:
    for d in t:
        if is_var(d):
            if d in declaracoes.keys():
                print(t[-1])
                i = declaracoes[d][1]
                f = declaracoes[d][2]
                if (t[-1] >= i):
                    if (i == f) or (t[-1] < f):
                        print("variavel ", d, " foi declarada")
                    else:
                        print("variavel ", d, " nao foi declarada previamente no escopo")
                else:
                    print("variavel ", d, " nao foi declarada previamente")
                    break
            else:
                print("variavel ", d, " nao foi declarada")
                break
# verificando se as operacoes estao corretas
def convertendo_(v):
    for i in v:
        if i == "'":
            return str
        elif i == ".":
            return float
        return int
def number(v):
    if v is (int or float):
        return True
    return False
#dicionario de atribucoes
print(trechos)
print(declaracoes)
for e in trechos:
    n = 0
    for v in e:
        if v in sinais:
            x = e[n-1]
            y = e[n+1]
            if x in declaracoes.keys():
                x = declaracoes[x][0]
            else:
                x = convertendo_(x)
            if y in declaracoes.keys():
                y = declaracoes[y][0]
            else:
                y = convertendo_(y)
            # print(x, y)
            if v == '%':
                if (x is int) and (y is int):
                    print("operacao de tipos valida para '%'")
                else:
                    print("operacao invalida para '%' ", x, "e", y)
            elif v == '=':
                if (x is int) and (y is not int):
                    print("atribuicao invalida, ", x, "e", y)
                if (x is str) and (y is not str):
                    print("atribuicao invalida, ", x, "e", y)
                if x is float:
                    y = declaracoes[x][0]
            else:
                if (number(x) and (y is str)):
                    y = declaracoes[x][0]

                elif (number(y) and (x is str)):
                    x = declaracoes[y][0]
        # verificado se as fucoes sao usadas corretamente
        if v == '(':
            x = e[n-1]
            v1 = []
            n += 1
            while e[n] != ')':
                # print(e[n])
                if (e[n] in declaracoes.keys()):
                    v1.append(declaracoes[e[n]][0])
                elif(e[n] != ','):
                    v1.append(convertendo_(e[n]))
                n += 1
            # print("v1",v1)
            v2 = []
            for d in declaracoes:
                z = declaracoes[d][1]
                # print(z)
                if d != x:
                    if z == declaracoes[x][1]:
                        v2.append(declaracoes[x][0])
            #print ("v2",v2)
            if v1 == v2:
                print("variaveis em ", x, " estao corretas",v1,v2)
            else:
                print("variaveis em ", x, " incorretas",v1, v2)                 
        n += 1
# print(declaracoes)