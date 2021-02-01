a="((F=2 && E=6) || (C=4 && D=5))"
out = {}
def check_syntax(a):
    lcnt=0
    rcnt=0
    for i in range(len(a)):
        if a[i] == '(':
            lcnt+=1
        if a[i] == ')':
            rcnt+=1
    if(lcnt!=rcnt):
        return 0
    return 1


def convert_to_json(a):
    syn=check_syntax(a)
    if syn==1:
        m = a.index('||')
        out['query']={"or":[0,0]}
        r1 = a.index('&&',0,m)
        eq1 = a.index('=',0,r1)
        eq2 = a.index('=',r1,m)
        s1 = { a[eq1-1] : int(a[eq1+1]),a[eq2-1] : int(a[eq2+1])}
        r2 = a.index('&&',m,len(a))
        eq3 = a.index('=',m,r2)
        eq4 = a.index('=',r2,len(a))
        s2 = { a[eq3-1] : int(a[eq3+1]),a[eq4-1] : int(a[eq4+1])}
        out['query']['or'][0]=s1
        out['query']['or'][1]=s2
        return out
    else:
        return "Syntax invalid"
        

print(convert_to_json(a))
