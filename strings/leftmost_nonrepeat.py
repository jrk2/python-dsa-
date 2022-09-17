import sys
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char =256
        l=[-1]*char
      
        for x in s:
            if l[ord(x)]==-1:
                l[ord(x)]=-2
            else:
                l[ord(x)]=-3  
        i=0  
        for x in s:
            if(l[ord(x)]==-2):
                return i
            i+=1
        return -1        
                 
        

a=Solution()
print(a.firstUniqChar('aabb') )          