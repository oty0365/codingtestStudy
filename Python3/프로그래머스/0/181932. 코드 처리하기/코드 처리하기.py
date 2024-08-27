def solution(code):
    mod = 0
    answer = ''
    
    for i in range(len(code)):
        if mod==0:
            if code[i]!='1':
                if i%2==0:
                    answer+=code[i]
            else:
                if mod==0:
                    mod = 1
                else:
                    mod = 0 
        else:
            if code[i]!='1':
                if i%2!=0:
                    answer+=code[i]
            else:
                if mod==0:
                    mod = 1
                else:
                    mod = 0 
                
    if len(answer)==0:
        return "EMPTY"
    return answer