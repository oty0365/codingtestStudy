"""
최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

"""
def solution(d, budget):
    answer = 0
    cost = budget
    d.sort()
    for i in d:
        cost=cost - i
        if(cost<0):
            break
        answer+=1
    return answer