#############################################
#      Máquina de Moore e Mealy             #
#      Autor: Paulo Dias                    #
#      Email: paulodiasprivado@gmail.com    #
#############################################

import random as random
print('========================================================\n')
print('Trabalho Circuitos Lógicos Digitais\n Aluno: Paulo Dias\n')
print('========================================================\n')
arqentrada = input('Insira o nome do arquivo: \n')
print('========================================================\n')
arquivo1 = open(arqentrada, 'r')
lista1 = arquivo1.readlines()
seq = lista1[0].replace('$',',',' ')
ent = lista1[1].replace('$',',',' ')

listaseq = seq.split()
listaent = ent.split()
listasai = []
ini = 0

################################################################
#   FOR PARA DETERMINAR AS SEQUÊNCIAS E DETERMINAS AS SAÍDAS   #
################################################################

for i1 in range(len(listaent)):
    if i1 == len(listaseq)-1:
        lista = []
        for i3 in range(len(listaseq)):
            lista.append(listaent[i3])
            if (i3<len(listaseq)-1):
                listasai.append('0')
        for i4 in range(len(listent)-len(listseq)):
            if (listaseq == lista):
                listasai.append('1')
                lista.pop(0)
                lista.append(listaent[i4+len(listaseq)])
            else:
                listasai.append('0')
                lista.pop(0)
                lista.append(listaent[i4+len(listaseq)])


#############################
#  ADICIONANDO OS ESTADOS   #
#############################

estados = []
count = 0
while(count == 0):
    dob = []
    for j1 in range(len(listaseq)):
         dob.append(1)
        dob.append(0)
        random.shuffle(dob)
        est = []
    for j2 in range(int(len(dob)/2)):
        est.append(dob[j2])
    if estados.count(est) == 0:
        estados.append(est)
    if len(estados) == 2**(len(listaseq)):
        count = 1
        
#############################
#     ORDENANDO ESTADOS     #
#############################
estados = sorted(estados)

#############################
#       INÍCIO TABELA       #
#############################
tab = open('tabela.txt', 'w')
tab.write('saída {} \n'.format(listasai))
listasai.insert(0, 'X')
tab.write('saída {} \n'.format(listasai))

#############################
#            MEALY          #
#############################
tab.write('Mealy \n'.format())
for k1 in range(len(estados)):
    estado1 = estados[k1]
    estado0 = estados[k1]
    estado1.pop(0)
    estado0.pop(0)
    estado1.append(1)
    estado0.append(0)
    tab.write('{} '.format(estados[k1]))
    tab.write('{} '.format(estado1))
    tab.write('{} \n'.format(estado0))
#############################
#         FIM MEALY         #
#############################


#############################
#           MOORE           #
#############################

tab.write('Moore \n'.format())
for k2 in range(len(estados)):
    estado1 = estados[k2]
    estado0 = estados[k2]
    estado1.pop(0)
    estado0.pop(0)
    estado1.append(1)
    estado0.append(0)
    if(estados[k2] == listaseq):
        tab.write('{}/1 '.format(estados[k2]))
    elif(estados[k2] != listaseq):
        tab.write('{}/0 '.format(estados[k2]))
    if(estado1 == listaseq):
        tab.write('{}/1 '.format(estado1))
    elif(estado1 != listaseq):
        tab.write('{}/0 '.format(estado1))
    if(estado0 == listaseq):
        tab.write('{}/1 \n'.format(estado0))
    elif(estado0 != listaseq):
        tab.write('{}/0 \n'.format(estado0))

#############################
#        FIM MOORE          #
#############################
tab.close()
print('======================================\n')
print('Um arquivo .txt foi gerado!\n')
sair = input('Aperte ENTER para sair!\n')
print('======================================\n')