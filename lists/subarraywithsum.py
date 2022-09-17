

def subarray(l,givensum):
   
    
    sum,j=0,0
    for  i in range(len(l)):
        sum+=l[i]
        while(givensum>sum):
            givensum-=l[j]
            j+=1
        if sum==givensum:
            return True

    return False 

    
    return False
    
    pass









if __name__=="__main__":

    l=[1,4,20,3,10,5]
    l1=[1,4,0,0,3,10,5]
    l2=[2,2,4]
    givensum=6
    print(subarray(l1,givensum))
