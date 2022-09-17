
def reverselist(l):
    reversedlist = [ l[x] for x in range(len(l)-1,-1,-1)]
    print(reversedlist)
    pass
 
def reverslist(l):
    m=0
    n=len(l)-1
    while m<n:
        l[m],l[n]=l[n],l[m]
        n-=1
        m+=1 

    print(l)    




if __name__=="__main__":
    
    l=[10,20,30,40,50,29,40]
    reverselist(l)
    reverslist(l)
