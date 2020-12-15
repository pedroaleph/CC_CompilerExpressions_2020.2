import tkinter.messagebox as ms

lexema = []
lexaux = []
aux = []
# espressoes, atributos, sinais..
exp = ['+', '-', '*', '/', '=', '<', '>', '>=', '<=','(', ')', '[', ']', '-=', '+=', '++', '--','"', ',', '{', '}',':', '?']
# tipo de variavel
tipo = ['int', 'float', 'char', 'string', 'double', 'long', 'if', 'for', 'in', 'do','while', 'else', 'printf', 'return','break', 'switch', 'case']
#numero
def  numero(num):
    try:
        int(num)
        return True
    except:
        try:
            float(num)
            return True
        except:
            return False

def varredura(linhas):
    # listas auxiliares
    lexema = []
    lexaux = []
    aux = []
    # espressoes, atributos, sinais..
    exp = ['+', '-', '*', '/', '=', '<', '>', '>=', '<=','(', ')', '[', ']', '-=', '+=', '++', '--','"', ',', '{', '}',':', '?', '%']
    # tipo de variavel
    tipo = ['int', 'float', 'char', 'string', 'double', 'long', 'if', 'for', 'in', 'do','while', 'else', 'printf', 'return','break', 'switch', 'case']

    # seperando os lexemas em linhas
    lexaux = linhas
    for x in lexaux:
        for y in x:
            aux.append(y)
            lexema.append(aux)
            # print (aux)
            aux = []
    # rotulando cada lexema
    n = 1
    for x in lexema:
        # caso " ; "
        if x[0] == ';':
            x.append('$')
        # caso num
        elif numero(x[0]):
            x.append('num')
        # caso expresão
        elif  x[0] in exp:
            x.append(x[0])
        #caso tipo de variável ou  funcao
        elif x[0] in tipo:
            x.append('PR')
        #caso ID
        else:
            x.append('ID')
        x.append(n)
        n-=-1
    '''
    for rotulo in lexema:
        print(rotulo)
    '''
    return lexema
