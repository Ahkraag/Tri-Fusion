# fonction coupeTab(t) qui renvoie deux tableaux Python contenant chacun, à un élément près, l'une des moitiés du tableau t

def coupeTab(t):
    j=[]
    m=[]
    if len(t)==0:
        return j,m
    for k in range(len(t)):
        if k<len(t)//2:
            j.append(t[k])
        else:
            m.append(t[k])
    return j,m

# Test #
t=[1,2,4,3,5,7,8,9]
t1,t2=coupeTab(t)
print(t1,t2)

# fonction fusionTab_Rec(t1,t2) qui, à partir des tableaux t1 et t2, triés par ordre croissant, renvoie un seul tableau contenant tous les éléments présents dans t1 et t2 (avec donc des doublons éventuels), et trié par ordre croissant

def fusionTab_Rec(t1,t2):
    if len(t1)==0:
        return t2
    if len(t2)==0:
        return t1
    if t1[0]<t2[0]:
        e=t1.pop(0)
        return [e]+fusionTab_Rec(t1,t2)
    e=t2.pop(0)
    return [e]+fusionTab_Rec(t1,t2)

# Test #

t1=[k+1 for k in range(0,10,2)]
t2=[k for k in range(0,12,2)]
print(t1,t2)
print(fusionTab_Rec(t1,t2))

# Même que au dessus mais en boucle

def fusionTab_Bcl(t1,t2):
    t=[]
    while len(t1)!=0 or len(t2)!=0:
        if len(t1)==0:
            t.append(t2.pop(0))
        elif len(t2)==0:
            t.append(t1.pop(0))
        elif t1[0]<=t2[0]:
            t.append(t1[0])
            t1.pop(0)
        else:
            t.append(t2[0])
            t2.pop(0)
    return t

# fonction triTab_fusionRec(t) qui renvoie un nouveau tableau contenant les valeurs du tableau t trié par ordre croissant par le principe du tri fusion (et utilisant la fonction fusionTab_Rec)

def triTab_fusionRec(t):
    if len(t)<=1:
        return t
    return fusionTab_Rec(triTab_fusionRec(coupeTab(t)[0]),triTab_fusionRec(coupeTab(t)[1]))

# Test #

t1=[k+1 for k in range(0,10,2)]
t2=[k for k in range(0,10,2)]
print(t1+t2)
print(triTab_fusionRec(t1+t2))

# Même que au dessus mais en boucle

def triTab_fusionBcl(t):
    if len(t)<=1:
        return t
    return fusionTab_Bcl(triTab_fusionBcl(coupeTab(t)[0]),triTab_fusionBcl(coupeTab(t)[1]))

# Test #

n=1972
t=[k for k in range(n,0,-1)]
print(triTab_fusionRec(t))

