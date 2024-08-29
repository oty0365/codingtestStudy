def solution(n):
    answer = 0
    n=str(n)
    a=[]
    b=""
    for i in range(0,len(n)):
        a.append(int(n[i]))
    a.sort(reverse = True)
    for i in range(0,len(a)):
        b+=str(a[i])
    answer =int(b)
    return answer