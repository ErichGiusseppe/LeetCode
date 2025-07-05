from math import ceil

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        for i in range(ceil(len(str_int)/2)): 
            if str_int[i]!=str_int[-(i+1)]:
                return False 
        return True