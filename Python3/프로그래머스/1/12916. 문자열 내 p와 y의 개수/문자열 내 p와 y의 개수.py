def solution(s):
    answer = False    
    pcount=0
    ycount = 0
    s=s.lower()
    for i in range(0,len(s)):
        if s[i]=="p":
            pcount+=1
        elif s[i]=="y":
            ycount+=1
    if(pcount==ycount):
        answer = True
    return answer