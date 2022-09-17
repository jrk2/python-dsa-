
def checksubsequence(s1,s2):
    
    i=0
    j=0
    while i<len(s2):
        k=i
        while j < len(s1) and i<len(s2):
            if s1[j]==s2[i]:
                i+=1
                j+=1
            else:
                j+=1
        if k==i:
            print("not subsequence")
            break;
    else:
        print("s2 is subsequence of s1")  

    
    pass
"""

    i,j=0,0
    while(i<len(s1) and j<len(s2)):
        if s1[i]==s2[j]:
            j+=1
        i+=1    
    if j==len(s2):
        return True
    else:
        return False     

"""




if __name__=="__main__":

    s1 = 'abc'
    s2 = 'c'

    checksubsequence(s1,s2)






