
from cmath import inf


def maxdiff(l):
    difflist=[]
    for i in range(len(l)-1):
        difflist.append(l[i+1]-l[i])
    print(difflist)
    max = float(-inf)
    for x in difflist:
        if x>max:
            max=x
    
    for i in range(len(difflist)-1):
        j=0
        sum=0
        while(i+j <len(difflist)):
            sum+=difflist[i+j]
            j+=1
            if sum>max:
                max=sum
               
    print(max)
                    


    
def maxDiff(arr):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
      
    for i in range( 1, len(arr) ):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
      
        if (arr[i] < min_element):
            min_element = arr[i]
    return max_diff


if __name__=="__main__":
    
    l=[7,9,5,6,3,2,]
    l1=[2,3,10,6,4,8,1]
    l2=[10,20,30]
    l3=[30,10,8,2]
    result = maxDiff(l)
    print(result)