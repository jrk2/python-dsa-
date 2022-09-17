

def palindromecheck(s):
    t=s[::-1]
    if s==t:
        return True
    else:
        return False    
    pass

def palindromecheck2(s):

    low=0
    high= len(s)-1

    while(low<high):
        if s[low]!=s[high]:
            return False

        low+=1
        high-=1

    return True     







if __name__=="__main__":
    s='ABBA'

    print(palindromecheck2(s))