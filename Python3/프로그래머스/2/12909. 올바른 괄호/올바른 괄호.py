"""
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

"""

def solution(s):
    answer = True
    open =[]
    for i in range(0,len(s)):
        if(s[i]=='('):
            open.append(0)
        elif(s[i]==')'):
            if(len(open)==0):
                print(1)
            else:
                open.pop()
    if(len(open)==0):
        answer = True
    else:
        answer = False
    if(s[0]==")"):
        answer = False

    return answer