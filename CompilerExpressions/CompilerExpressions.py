from tkinter import *
import tkinter.scrolledtext as st
import tkinter.filedialog as fd
import tkinter.messagebox as ms
import os
import varredor
import analisador_lexico
import analisador_semantico
import codigo_intermediario
import codigo_simbolico

# lista para armazena os dados da analise sintatica
dados = []
codigo = Tk(className=" CompilerExpressions")
texto = st.ScrolledText(codigo, width=50, height=20)

def lendo_arquivo(linhas):
    entrada = open('arquivo.txt', 'r')
    for line in entrada:
        line = line.replace(';', '\n')
        line = line.replace('(', ' ( ').replace(')', ' ) ')
        line = line.replace('{', ' { ').replace('}', ' } ')
        line = line.split()
        linhas.append(line)
    entrada.close()
    #print(linhas)
    return linhas

def save_command(self):
    data = texto.get('1.0', 'end-1c')
    if len(data) == 0:
        ms.showerror('ERRO!', 'Arquivo Vazio')
    else:
        arquivo = open('arquivo.txt', 'w')
        arquivo.write(data)
        arquivo.close()
        ms.showinfo('Sucesso!', 'Arquivo Salvo')
def lexic_command(self):
    linhas = []
    linhas = lendo_arquivo(linhas)
    linhas = varredor.varredura(linhas)
    for l in linhas:
        if l[1] != 'ID':
            l.clear()
    linhas  = list(filter(None, linhas))
    #print(linhas)
    c = False
    for l in linhas:
        c = analisador_lexico.automatov(l[0])
        if c == False:
            break
    if c:
        ms.showinfo('Sucesso!', 'Analise Lexica Concluida')

def sintatic_command(self):
    linhas = []
    linhas = lendo_arquivo(linhas)
    #print(linhas)
    for l in linhas:
        #print(l)
        if l[0] in analisador_semantico.tipo.keys():
            l.pop(0)
        if (len(l) == 1) or (l[1] != '='):
            l.clear()
    linhas  = list(filter(None, linhas))
    print(linhas)
    if (codigo_intermediario.analise_sintatica(linhas, dados)):
        ms.showinfo('Sucesso!', 'Analise Sintatica Concluida')
    
def semantic_command(self):
    linhas = []
    linhas = lendo_arquivo(linhas)
    #print(linhas)
    if(analisador_semantico.semantico(linhas)):
        ms.showinfo('Sucesso!', 'Analise Semantica Concluida')

def code_command(self):
    if dados != []:
        codigo_intermediario.codigo_intermediario(dados.copy())
        os.startfile("codigo_intermediario.txt")


    dados.clear()
def code_s_command(self):
    codigo_simbolico.gerar_codigo()
    os.startfile("codigo_simbolico.txt")

def exit_command():
    if ms.askokcancel("Sair", "voce realmente deseja?"):
        codigo.destroy()

menu = Menu(codigo)
codigo.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Arquivo", menu=filemenu)
filemenu.add_command(label="Salvar", command= lambda : save_command(codigo))
filemenu.add_command(label="Analise Lexica", command= lambda : lexic_command(codigo))
filemenu.add_command(label="Analise Sintatica", command= lambda : sintatic_command(codigo))
filemenu.add_command(label="Analise Semantica", command= lambda : semantic_command(codigo))
filemenu.add_command(label="Gerar Codigo Intermediario", command= lambda : code_command(codigo))
filemenu.add_command(label="Gerar Codigo em Liguagem Simbolica", command= lambda : code_s_command(codigo))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

texto.pack()
codigo.mainloop()