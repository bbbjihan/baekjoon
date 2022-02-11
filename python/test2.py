def check_balancedstr(p):
    if p.count('(') == p.count(')'):
        return True
    return False

def check_goodstr(p):
    queue = []
    for i in p:
        if i == '(':
            queue.append(0)
        elif len(queue) == 0:            
            return False
        else:
            queue.pop()
    if len(queue) == 0:
        return True
    return False

def sol4_4(p):
    tmp = ''
    for i in range(1,len(p)-1):
        if p[i] =='(':
            tmp+=')'
        else:
            tmp+='('
    return tmp
        
def sol(p):
    leng = len(p)
    if leng == 0:
        return ''
    for i in range(leng):
        if check_balancedstr(p[0:i+1]):
            u = p[0:i+1]
            v = p[i+1:leng]
            break
    if check_goodstr(u):
        return u + sol(v)
    else:
        return '('+sol(v)+')' + sol4_4(u)

def solution(p):
    answer = ''
    if check_goodstr(p):
        return p
    return sol(p)

print(solution('()))((()'))