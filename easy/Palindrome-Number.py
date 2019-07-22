class Solution(object):
    #without string conversion        
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not x:
            return True
    
        if x<0:
            return False
        
        n = x
        r = 0

        while(n>0):
            r = r*10 + (n%10)
            n /= 10
    
        return r == x
 
