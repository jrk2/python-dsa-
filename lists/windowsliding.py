
def windowsliding(l,k):
   
    initialsum=0
    n=len(l)
    for x in range(k):
        initialsum+=l[x]
    i=1 
    print(initialsum)
    max=initialsum
    while(i+k-1<n):
        initialsum=initialsum-l[i-1] + l[i+k-1]
        
        if initialsum>max:
            max=initialsum
        i+=1
        pass

    print(max)



    
    pass




if __name__=="__main__":
    
    l=[10,20,30,40,50,29,40]
    l1=[1,8,30,-5,20,7]
    k=3
    windowsliding(l1,k)
    