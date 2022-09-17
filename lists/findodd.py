## use if list values are not integers 
'''
def findodd(l):
    mydict = {}

    for x in l:
        try:
            mydict[x]
        except:
            mydict[x]=0
        mydict[x]+=1      
     
    for x in mydict.keys():
        if mydict[x]%2!=0:
            print(x)          
    pass


'''
## using bitwise xor operation as x^0=0, x^x=0
def findodd(l):
    y=0
    for x in l :
        y=y^x

    print(y)    
        
    pass


if  __name__ == "__main__":

    l =[10,20,30,30,10,20,30,30,20]
    l1 = [10,20,20,30,10]
    findodd(l)


