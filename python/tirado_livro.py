# Hello World program in Python
from math import *

#Tudo funciona

for item in range(9, -1, -1): print(item)
print(" ")
for item2 in range(10): print(item2) 
print(" ")    
s1=set(range(3))
s2=set(range(10,7,-1))
s3=set(range(2,10,2))
numero=sorted(s3)
print 's1:',s1,'\ns2:',s2,'\ns3:',s3
print 's3 modificado:',numero
print(" ")
teste=range(0,10)
print teste
for i in range(0,10): print i
y=xrange(0,10)
print y
xrange(10)
print(" ")
numeros=[4,2,6,1,3]
numeros_ordenados=sorted(numeros)
#print (numeros) and (numeros_ordenados)
#print numeros_ordenados
print "numeros=",numeros, "\nnumeros_ordenados=",numeros_ordenados
print("")
palavras=["chocolate","biscoito","cafe","suco","feijao","arroz"]
palavras_ordenadas=sorted(palavras)
print "palavras=",palavras, "\npalavras_ordenadas=",palavras_ordenadas
print("")
print "%3d\n%3d" % (50,150)
print("")

dic={'nome':'Shirley Manson','banda':'Garbage'}
print "nome=",dic['nome'], "\n", "\nbanda=",dic['banda']
dic['album']='Version 2.0'
print "nome=",dic['nome'], "\n", "\nbanda=",dic['banda'], "\nalbum=",dic['album']
del dic['album']
print("")
#progs e seus albuns
progs={'Yes':['Close to the Edge','Fragil'],'Genesis':['Foxtrat','The nursery Crime'],'ELP':['Brain Salad Surgery']}
#Mais progs
progs['King Crimson']=['Red','Discipline']
#items() retorna uma lista de
#tuplas com a chave e o valor
for prog,albuns in progs.items():
    print prog,'=>',albuns
#Se tiver 'ELP', deleta
if progs.has_key('ELP'):
    del progs['ELP']
print("")

#*************************
#Exemplo de matriz esparsa
#*************************
# Matriz esparsa implementada
# com dicionário
# Matriz esparsa é uma estrutura
# que só armazena os valores que
# existem na matriz

#dim=6,12
dim=7,12
mat={}
#Tuplas são imutaveis
#cada tupla representa
#uma posicao na matriz
mat[3,7]=3
mat[4,6]=5
mat[6,3]=7
mat[5,4]=6
mat[2,9]=4
mat[1,0]=9
for lin in range(dim[0]):
    for col in range(dim[1]):
        #metodo get(chave,valor)
        #retorna o valor da chave
        #no dicionário ou se a chave
        #não existir, retorna o
        #segundo argumento
        print mat.get((lin,col),0),
    print
print(" ")

#**********************
#Gerando matriz esparsa
#**********************
#Matriz em forma de string
matriz = '''0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 4 0 0 
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 5 0 0 0 0 0
0 0 0 6 0 0 0 0 0 0 0 0'''

mat = {}
 
#Quebra a matriz em linhas
for lin, linha in enumerate(matriz.splitlines()):
    #Quebra a linha em colunas
    for col, coluna in enumerate(linha.split()):
        colune = int(coluna)
        #Coloca a coluna no resultado
        #se for diferente de zero
        if coluna:
            mat[lin,col] = coluna
print mat
#Some um nas dimensoes pois a contagem comeca em zero
print 'Tamanho da matriz completa:',(lin + 1) * (col + 1)
print 'Tamanho da matriz esparsa:',len(mat)
print(" ")
s = 'n o m e'
s_1 = s.split()      # ['n', 'o', 'm', 'e']
s_2 = s.split(" ")   # ['n', 'o', 'm', 'e']

print "S_1:",s_1, "\nS_2:",s_2

print(" ")
test = 'This is just a simple string.' 
test2 = test.split()
print test2

def rgb_html(r=0, g=0, b=0):
    '''Converte R, G, B em #RRGGBB'''
    return '#%02x%02x%02x' % (r,g,b)
def html_rgb(color='#000000'):
    '''Converte #RRGGBB em R, G, B'''
    if color.startswith('#'): color = color[1:]
    r = int(color[:2],16)
    g = int(color[2:4],16)
    b = int(color[4:],16)
    
    return r, g, b #uma sequencia
     
print rgb_html(200, 200, 255)
print rgb_html(b=200, g=200, r=255)
print html_rgb('c8c8ff')
print(" ")
# *args - argumentos sem nome (lista)
# **karjs - argumentos com nome (dicionário)
def func(*args, **kargs):
    print args
    print kargs
func('peso', 10, unidade='k')

#exemplo serie de fibonacci sem recursao
def fib(n):
    """Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) se n > 1
    fib(n) = 1 se n <= 1
    """
    
    #Dois primeiros valores
    I = [1, 1]
    
    #Calcula os outros
    for i in range(2, n + 1):
        I.append(I[i - 1] + I[i - 2])
    return I[n]
#mMostrar Fibonacci de 1 a 5
for i in [1, 2, 3, 4, 5]:
    print i, '=>', fib(i)
print("")
import os
import sys
import platform

def uid():
    """
    uid() -> retorna a identificação do usuário
    corrente ou none se não for possível idenficar
    """
    
    # Variaveis de ambiente para cada
    # sistema operacional
    us = {'Windows': 'USERNAME', 'Linux': 'USER'}
    u = us.get(platform.system())
    return os.environ.get(u)
print 'Usuarui:', uid()
print 'plataforma:', platform.platform()
print 'Diretório corrente:', os.path.abspath(os.curdir)
exep, exef = os.path.split(sys.executable)
print 'Executavel:', exef
print 'Diretório do executavel:', exep
####
#TEMPO
import time
print time.localtime()
print time.asctime()

print ' O programa levou', time.clock(), 'segundos ate agora...'
for i in xrange(5):
    time.sleep(1)
    print i + 1, 'segundos(s)'

import datetime
# datetime() recebe como parametros:
# ano, mes, dia, hora, minuto, segundo
# e retorna um objeto do tipo datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)

# Objetos date e time pode ser criados
# a partir de um objeto datetime
data = dt.date()
hora = dt.time()

# Quanto tempo falta para 31/12/2020
dd = dt - dt.today()

print 'Data:', data
print 'Hora:', hora
print 'Quanto tempo falta para 31/12/2020:', str(dd).replace('days','dias')
print(" ")
import random

# Cria um arquivo com 25 numeros randômicos
with file('temp.txt', 'w') as temp:
    for y in range(5):
        for x in range(5):
            #print >> "grava a saida do comando no arquivo indicado"
            print >> temp, '%.2f' % random.random(),
        print >> temp
# Exibe o conteúdo do arquivo
with file('temp.txt') as temp:
        for i in temp:
            print i,
# Fora dos Blocos, o arquivo está fechado
# Isso gera uma exceção ValueError: I/O operation on closed file
print >> temp

print(" ")
from types import ModuleType

def info(n_obj):
    
    # Cria uma referencia ao objeto
    obj = globals()[n_obj]
    # Mostra informações sobre o objeto
    print 'Nome do objeto:', n_obj
    print 'Identificador:', id(obj)
    print 'Tipo:', type(obj)
    print 'Reprensentação:', repr(obj)
    
    # Se for um modulo
    if isinstance(obj, ModuleType):
        print 'itens:'
        for item in dir(obj):
            print item
    print
# Mostrando as informações
for n_obj in dir():
    info(n_obj)
print ("")
import types

s = 23
if isinstance(s, types.StringType):
    print 's é uma string'
else:
    print 's=', s

print ("")
#***************************
# Mapeamento
# aplicar uma funcao a todos os itens de uma sequencia
# gerando outra lista
# contendo os resultados
# e com o mesmo tamanho da lista inicial
# mapeamento => funcao map()

nums =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# log na base 10
from math import log10
print map(log10, nums)
# Dividindo por 3
print map(lambda x: x / 3, nums)
# sempre retorna uma lista
print ("")
# Filtragem
# uma funcao é aplicada em todos os itens
# de uma sequencia, se a funcao retornar um valor
# que seja avaliadocomo verdadeiro,
# o item original fará parte da sequencia resultante
# filtragem => filter()
