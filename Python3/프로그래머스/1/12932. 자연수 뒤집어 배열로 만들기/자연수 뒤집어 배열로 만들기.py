def solution(n):
    answer = []
    n=str(n)
    print(n)
    for i in range(len(n),0,-1):
        answer.append(int(n[i-1]))
    return answer