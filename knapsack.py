import random

def keygen(k):
    s=[]
    s.append(random.randint(1,24))
    aux = s[0]
    for i in range(1,k):
        s.append(random.randint(aux+1,aux+random.randint(2,54)))
        aux+=s[i]
    m = getm(s)
    n = getn(m,s)
    p=[]
    for number in s:
        p.append( (n*number) % m)
    return (p, s, m, n)

def cipher(msg, p):
    list=[]
    k=len(p)
    while len(msg) >= k :
        chunk = msg[:k]
        del msg[:k]
        aux=[]
        indexOfp = 0
        for binary in chunk:
            if indexOfp < k:
                if(binary==1):
                    aux.append(p[indexOfp])
                indexOfp+=1
            else:
                indexOfp = 0
        list.append(sum(aux))
    return list

def decipher(msg, s, m, n):
    modular_inverse = xEuclid(n,m)
    for number in msg:
        aux = msg.pop(0)
        msg.append((aux*modular_inverse) % m)
    list = []
    s = sorted(s,reverse=True)
    for number in msg:
        aux_s = s[:]
        list.append(pickBest(aux_s,number))
    return sum(list,[])

def pickBest(s,left):
    list = []
    while len(s) > 0:
        c = s.pop(0)
        if c <= left:
            list.append(1)
            left -= c
        else:
            list.append(0)
    return list[::-1]

def xEuclid(d,f):
    x1, x2, x3 = 1, 0, f
    y1, y2, y3 = 0, 1, d
    while True:
        if y3==0:return x3
        if y3==1:return y2+f
        q=x3/y3
        x1, x2, x3, y1, y2, y3 = y1, y2, y3, x1-q*y1, x2-q*y2, x3-q*y3

def getm(s):
    aux = sum(s) + random.choice(s)
    if aux%2==0: return aux+1
    else: return aux

def getn(m,s):
    aux = random.randint(random.choice(s),m-1)
    while(True):
        if(aux%2!=0 and gcd(aux,m)): return aux
        else: aux-=1

def gcd(a, b):
    while b > 0: a, b = b, a % b
    return a
