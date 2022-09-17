import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        pattern=r'\s+'
        l=re.split(pattern,s)
        l.reverse()
        print(l)
        st=' '.join(l)
        print(st)
        return st 

        