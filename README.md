# Máquina Mealy e Moore

## Introdução 🤓
Escrever um programa em Python que recebe como entrada uma sequência binária e gera como saída as tabelas de transição das máquinas Moore e Mealy do detector de sequência correspondente.

## Funcionamento 🖥️

Ao ler um arquivo .txt, o programa pega a sequência binária de entrada e vai gerando as saídas nas tabelas. As sequências são determinadas no primeiro <i>for</i>.
```
for i1 in range(len(listaent)):
    if i1 == len(listaseq)-1:
        lista = []
        for i3 in range(len(listaseq)):
            lista.append(listaent[i3])
            if (i3<len(listaseq)-1):
                listasai.append('0')
    
Continua [...]
```
Após isso há a criação dos estados e seu ordenamento.
```
estados = []
count = 0
while(count == 0):
    dob = []
    for j1 in range(len(listaseq)):
         dob.append(1)
        dob.append(0)
[...] 
#############################
#     ORDENANDO ESTADOS     #
#############################
estados = sorted(estados)
```

Por fim, é gerada a tabela e as espeficifações são feitas para Moore e Mealy.

## Execução do arquivo 🏃

> python maquinasmealymoore.py
