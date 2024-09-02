def solution(a, d, included):
    dgca = []
    answer = 0
    c=0
    for i in range(len(included)):
        c=a+d*i
        dgca.append(c)
        if included[i] ==True:
            answer+=c
    
    return answer