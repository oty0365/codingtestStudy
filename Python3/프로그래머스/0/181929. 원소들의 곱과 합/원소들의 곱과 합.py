def solution(num_list):
    answer = 0
    mul=1
    add=0
    for i in range(len(num_list)):
        mul*=num_list[i]
        add+=num_list[i]
    add=add**2
    if add>mul:
        answer=1
    elif add<mul:
        answer=0
    return answer