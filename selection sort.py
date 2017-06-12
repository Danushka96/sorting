l=[1,2,5,8,9,7,7,1,5,4]
ls=[]
def checkme(x):
    min=x[0]
    for i in range (0,len(x)):
        if min>x[i]:
            min=x[i]
    l.remove(min)
    ls.append(min)
    if not l==[]:
        checkme(l)
    else:
        print(ls)

checkme(l)
