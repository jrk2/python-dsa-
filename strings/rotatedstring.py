
def rotatedstring(s,t):
    if len(s)!=len(t):
        return False

    temp=s+s
    return temp.find(t)!=-1       
    pass



if __name__=="__main__":
    s='ABCD'
    t='BCAD'

    print(rotatedstring(s,t))