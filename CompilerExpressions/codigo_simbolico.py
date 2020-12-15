# dicionario de oepradores
operadores = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div', '%': 'div'}
# operacoes de multiplicacao e onde sao armazenados
mul = {'*': 'ax', '/': 'ax', '%': 'dx'}
#lendo o codigo intermediario
def gerar_codigo():
    codigo = []
    entrada = open('codigo_intermediario.txt', 'r')
    for linha in entrada:
        linha = linha.split()
        linha.pop()
        codigo.append(linha)

    entrada.close()

    print(codigo)

    #declarando variaveis no codigo simbolico
    variaveis = []
    for line in codigo:
        n = 0
        while n < len(line):
            if line[n] not in variaveis:
                variaveis.append(line[n])
            n += 1

    #print(variaveis)

    #escrevendo operacoes
    def operation(line):
        tamanho = len(line)
        m = ""
        if tamanho == 3:
            if line[2] in variaveis:
                m = '\nmov ax,' + line[2] + '\n'
                m += 'mov ' + line[0] + ', ax\n'
            else:
                m = '\nmov ' + line[0] + ', '+ line[2] + '\n'
        else:
            if line[3] in mul.keys():
                m = '\nmov ax, ' + line[2] + '\n'
                m += 'mov bx, ' + line[4] + '\n'
                m += operadores[line[3]] + ' bx\n'
                m += 'mov ' + line[0] + ', '+ mul[line[3]] + '\n'

            else:
                m = '\nmov ax, ' + line[2] + '\n'
                m += operadores[line[3]] + ' ax, ' + line[4] + '\n'
                m += 'mov ' + line[0] + ', ax\n'

        return m


    #escrevendo no codigo em linguagem simbolica

    saida = open('codigo_simbolico.txt', 'w')
    saida.write('org 100h\n\n')
    saida.write('; variaveis\n\n')
    for var in variaveis:
        saida.write(var + ' DW ' + '0\n')

    saida.write('\n; expressoes\n')

    for line in codigo:
        saida.write(operation(line))

    saida.write('\nret')

    saida.close()