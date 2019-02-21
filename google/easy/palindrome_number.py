class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype:ef bool
        """
        if x<0 or (x%10==0 and x!=0):
            return False
        return self._reverse_half_number(x)
                
    def _reverse_half_number(self,x):
        reverse = 0
        while x and x>reverse:
            remainder = x%10
            x = x/10
            reverse = reverse*10+remainder
            
        return reverse==x or reverse/10==x
        
