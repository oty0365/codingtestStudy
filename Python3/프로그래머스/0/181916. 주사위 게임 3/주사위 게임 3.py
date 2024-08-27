def solution(a, b, c, d):
    answer = 0
    #abcd
    if(a==b==c==d):
        answer=1111*a
    #abd,c
    elif(a==b==d!=c):
        answer=(10*a+c)**2
    #acd,b
    elif(a==c==d!=b):
        answer=(10*a+b)**2
    #bcd,a
    elif(b==c==d!=a):
        answer=(10*b+a)**2
    #abc,d
    elif(a==b==c!=d):
        answer=(10*a+d)**2
    #ab,cd
    elif(a==b!=c==d):
        answer=(a+c)*abs(a-c)
    #ac,bd
    elif(a==c!=b==d):
        answer=(a+b)*abs(a-b)
    #ad,bc
    elif(a==d!=b==c):
        answer=(a+b)*abs(a-b)
    #ab,d/c
    elif(a==b!=d!=c):
        answer=d*c
    #ac,d/b
    elif(a==c!=d!=b):
        answer=d*b
    #ad,b/c
    elif(a==d!=b!=c):
        answer=b*c
    #cd,a/b
    elif(c==d!=a!=b):
        answer=a*b
    #bd,a/c
    elif(d==b!=a!=c):
        answer=a*c
    #bc,d/a
    elif(b==c!=d!=a):
        answer=d*a
    #a/b/c/d
    else:
        answer = min(a,b,c,d)
        
    return answer