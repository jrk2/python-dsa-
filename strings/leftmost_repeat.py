
def leftmost(s):
    for x in s:
        if s.count(x)>1:
            print(s.index(x))
            break
    else:
        print('-1')
  
def leftmost1(s):
    count = [0]*256 
    for i in range(len(str)):
        count[ord(s[i])]+=1

    for i in range(len(str)):
       if  count[ord(s[i])]>1:
           return i 

    return -1       


if __name__=="__main__":

    s='abccb'

    leftmost(s)