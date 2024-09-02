def solution(names):
    answer = []
    fivecount=0
    for i in range(len(names)):
        if fivecount==0:
            answer.append(names[i])
            fivecount=5
        fivecount-=1
    return answer