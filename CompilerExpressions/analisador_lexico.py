import string
import tkinter.messagebox as ms
# alfabeto
alfabeto = {'a' : 0, 'b': 1}
def verifica(i):
    if i.isalpha() or (i == '_'):
        return 'a'
    elif i.isalnum():
        return 'b'
    return i
def automatov (L):
    '''matriz do automato de variáveis'''
    M = [[ 1, 1], [ -1, 1]] 
    e = 0 
    for i in L:
        l  = verifica(i)
        #print(l)
        if l in alfabeto.keys():
            e = M[alfabeto[l]][e]
            if e == -1:
                ms.showerror('ERRO!', 'variavel nao declarada corretamente\n' + L)
                return False
        else:
            ms.showerror('ERRO!', 'simbolo nao aceito\n'+ i + ' em ' + L)
            return False
    '''Estado Final '''
    if e == 1:
        print ('variavel reconhecida: '+ L)
        return True
    else:
        ms.showerror('ERRO!', 'variavel nao reconhecida: ' + L)
        return False
