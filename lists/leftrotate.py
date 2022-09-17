
from collections import deque

#0(nd) time
def leftrotate1(l,n):
    for x in range(n):
        l.append(l.pop(0))
    print(l)
    pass

def leftrotate2(l,n):
    dq=deque(l)
    dq.rotate(-n)
    l = list(dq)
    print(l)

# needs auxilliary space 0(nd) time 
def leftrotate3(l,n):
    l = l[n:] + l[:n]
    print(l)
    pass

def reverse(l,b,e):
    while(b<e):
        l[b],l[e]=l[e],l[b]
        b+=1
        e-=1

def leftrotate4(l,d):
    n = len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)
    print(l)
    pass


if __name__=="__main__":
    
    l=[10,20,30,40,50,29,40]
    leftrotate4(l,2)
 