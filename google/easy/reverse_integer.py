class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversex = 0
        negative = (x<0)
        x = -x if negative else x
        
        while x:
            remainder = x%10
            x = x/10
            reversex = reversex*10 + remainder
        reversex = -reversex if negative else reversex
        if reversex > 2**31-1 or reversex< -2**31:
            return 0
        return reversex
        

