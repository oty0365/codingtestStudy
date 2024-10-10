def solution(absolutes, signs):
    answer = 0
    neg=0
    for i in range(len(absolutes)):
        if(signs[i]):
            neg=1
        else:
            neg=-1
        answer+=absolutes[i]*neg
    return answer