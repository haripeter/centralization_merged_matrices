#1. matrix:
f=open('C:/Users/Peti/Desktop/Network Lab/Centrality of merged matrices/2013_3_6_a.txt', 'r')

#2. matrix:
g=open('C:/Users/Peti/Desktop/Network Lab/Centrality of merged matrices/2013_3_6_b.txt', 'r')

#3. matrix:
h=open('C:/Users/Peti/Desktop/Network Lab/Centrality of merged matrices/2013_3_6_c.txt', 'r')

def header(adat):
#levágja a headert és megtisztítja
    doboz=[]
    for i in adat:
        doboz.append(i.split('\t'))
    return(doboz)
lista=header(f.readlines())
lista1=header(g.readlines())
lista2=header(h.readlines())

def header_select(adat):
    fejlec=[]
    for i in adat[0]:
        if len(i)>0:
            fejlec.append(i)
    return(fejlec)

header=header_select(lista)
header=[i.strip('\n') for i in header]

header1=header_select(lista1)
header1=[i.strip('\n') for i in header1]

header2=header_select(lista2)
header2=[i.strip('\n') for i in header2]

def header_egyezes(header, header1, header2):
    if header != header1:
        print("mátrix 1 és 2 header nem egyezik")
    if header != header2:
        print("mátrix 1 és 3 header nem egyezik")
    if header1 != header2:
        print("mátrix 2 és 3 header nem egyezik")

print(header)

def cut_first_column(adat):
#levágja az első oszlopot:
    doboz=[]
    for i in adat:
        doboz=adat[1:]
    return(doboz)
box=cut_first_column(lista)
box_1=cut_first_column(lista1)
box_2=cut_first_column(lista2)

def cut_first_row(adat):
#levágja az első sort:
    doboz=[]
    for i in adat:
        doboz.append(i[1:])
    return(doboz)
box1=cut_first_row(box)
box1_1=cut_first_row(box_1)
box1_2=cut_first_row(box_2)

def cut_last_column(adat):
#kivágja az utolsó oszlopot:
    doboz=[]
    for i in adat:
        doboz.append(i[-1])
    return(doboz)
box2=cut_last_column(box1)
box2_1=cut_last_column(box1_1)
box2_2=cut_last_column(box1_2)

def clean_last_column(adat):
#kivágja a newline chart az utolsó oszlopból:
    doboz=[]
    for i in adat:
        if len(i) > 1:
            doboz.append(i[:-1])
        else:
            doboz.append(i)
    return(doboz)
box3=clean_last_column(box2)
box3_1=clean_last_column(box2_1)
box3_2=clean_last_column(box2_2)

def magic(box1):
#a letisztított utolsó oszlopot bevágja az newlinecharos utolsó oszlop helyére:
    g=0
    for i in box1:
        i[-1]=box3[g]
        g=g+1
    return(box1)

def magic_1(box1_1):
    g=0
    for i in box1_1:
        i[-1]=box3_1[g]
        g=g+1
    return(box1_1)

def magic_2(box1_2):
    g=0
    for i in box1_2:
        i[-1]=box3_2[g]
        g=g+1
    return(box1_2)

#making int in list of lists instead of str
box1=[[int(g) for g in x] for x in box1]
box1_1=[[int(g) for g in x] for x in box1_1]
box1_2=[[int(g) for g in x] for x in box1_2]

print(box1)
print(box1_1)
print(box1_2)

def merge_boxes(doboz1, doboz2, doboz3):
    f=[]
    y=[]
    for a, b, c in zip(doboz1, doboz2, doboz3):
        v=0
        while v < len(a):
            y.append(a[v]+b[v]+c[v])
            v=v+1
    b=len(a)
    o=0
    t=b
    while b < len(y)+1:
        f.append(y[o:b])
        o=b
        b=b+t
    return(f)

q=merge_boxes(box1, box1_1, box1_2)

##transzformált adatmátrix (data): az 1-nél nagyobb értékek 1-es értéket kapnak:
data=[[i if i == 0 else 1 for i in x] for x in q]
#print(data)

##transzformált adatmátrixban összeadja az oszlopokhoz tartozó értékeket:
list_of_indegree_centralization=[sum(i) for i in zip(*data)]

def indegree_of_centralization(lista):
    indegree_of_cent=[]
    for i in lista:
        indegree_of_cent.append(float(i/(len(lista)-1)))
    return(indegree_of_cent)

indegree_of_cent=indegree_of_centralization(list_of_indegree_centralization)

##-------OUTDEGREE CENTRALITÁS--------
##transzformált adatmátrixban összeadja a sorokhoz tartozó értékeket:
list_of_outdegree_centralization=[]
for i in data:
    list_of_outdegree_centralization.append(sum(i))

##print(list_of_outdegree_centralization)

def outdegree_of_centralization(lista):
    outdegree_of_cent=[]
    for i in lista:
        outdegree_of_cent.append(float(i/(len(lista)-1)))
    return(outdegree_of_cent)

outdegree_of_cent=outdegree_of_centralization(list_of_outdegree_centralization)

# Print it!

print("indegree_of_cent")
kl=0
while kl<len(indegree_of_cent):
    print(header[kl], indegree_of_cent[kl])
    kl=kl+1

print("outdegree_of_cent")
km=0
while km<len(outdegree_of_cent):
    print(header[km], outdegree_of_cent[km])
    km=km+1
