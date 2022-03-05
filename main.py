a=input()
if a.find('+')>0:
    b,c=a.split('+')
    b=int(b)
    c=int(c)
    print(b+c)
elif a.find('-')>0:
    b,c=a.split('-')
    b=int(b)
    c=int(c)
    print(b-c)
elif a.find('/')>0:
    b,c=a.split('/')
    b=float(b)
    c=int(c)
    print("%.2f" %(b/c))
elif a.find('*')>0:
    b,c=a.split('*')
    b=int(b)
    c=int(c)
    print(b*c)
