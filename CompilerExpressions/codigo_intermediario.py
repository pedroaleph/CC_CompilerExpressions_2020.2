import analisador_sintatico.analisador_preditivo as asp
import analisador_sintatico.analisador_precedencia_fraca as apf
import analisador_sintatico.arvore_sintatica as arsp
import analisador_sintatico.as_apf as arpf
import string
# lista principal a ser percorrida
operadores = ['+', '-', '*', '/']
exps = []
n_line = 0
# arquivo de teste
arquivo = open('expressao.txt', 'r')
for linha in arquivo:
    linha = linha.split()
    linha.append(n_line)
    exps.append(linha)
    n_line -= - 1
arquivo.close()
print(exps)
s = ""
for x in exps:
    n = 0
    s = ""
    for y in x:
        if y != x[-1]: 
            if (x[n + 1] == '=') or (x[n + 1] not in operadores):
                print(y)
                s += y
            elif (y ==  '=') or y.isnumeric():
                print(y)
                s += y
            n += 1
print(s)
V = []
p = ""
for l in s:
    V.append(l)
    if l != '=':
        p += 'i'
    else:
        p += l

print(V)
print(p)
a = []
if (asp.automatoM(p, asp.gramatica_A)):
    a = asp.a
    a = arsp.arvore_sintatica(a)
    a = arsp.ar_simp(a)
s = list(s[::-1])
#print(s)
#colocando as variaveis corretas
def correcao(a):
    #print(a)
    #print(s)
    if s != "":
        a[1] = s.pop()
        s.pop()
        if len(a[2]) > 1:
            correcao(a[2])
        else:
            a[2] = s.pop()
    return a
a = correcao(a)
print(a)
cod_in = []
def escrevendo(a):
    #print(a[2])
    if len(a[2]) > 1:
        a[2] = escrevendo(a[2])
    m = a[1][0] + " " + ':' + a[0][0] + " " + a[2][0] + " ;\n"
    cod_in.append(m)
    return a[1]
escrevendo(a)
print(cod_in)

# arquivo de saida com a espressao intermediaria

saida = open('codigo_intermediario.txt', 'w')
saida.writelines(cod_in)
saida.close()





