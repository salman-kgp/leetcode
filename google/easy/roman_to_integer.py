class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        current_ptr = 0
        result = 0
        while current_ptr<len(s):
            if current_ptr+1<len(s) and roman_to_int_map[s[current_ptr]]<roman_to_int_map[s[current_ptr+1]]:
                result+=(roman_to_int_map[s[current_ptr+1]]-roman_to_int_map[s[current_ptr]])
                current_ptr+=2
                continue
            result+=roman_to_int_map[s[current_ptr]]
            current_ptr+=1
        return result
                        

