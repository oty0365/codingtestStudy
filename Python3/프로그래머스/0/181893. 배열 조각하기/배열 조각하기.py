def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i%2==0:
            arr=arr[0:query[i]+1]
        else:
            arr=arr[query[i]:len(arr)+1]
    answer=arr
    return answer