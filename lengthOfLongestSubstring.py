def lengthOfLongestSubstring(s: str) -> int:
        if len(s)<=1:
            return len(s)
        i,j = 0, 1
        seen = {}
        seen[s[i]] = i
        #seen[s[j]] = 1

        max_number = 0
        
        while j < len(s) :
            if s[j] in seen and seen[s[j]] >= i and (j != seen[s[j]] or s[i] == s[j]) : #and i <= seen[s[j]]
                
                max_number = max(max_number, j - i )
                i = seen[s[j]]+1 #i+1 if (seen[s[j]] <= i ) else
                seen[s[j]] = j
                j = j+1 if j == i else j
            else:
                max_number = max(max_number, j - i + 1)
                seen[s[j]] = j
                j += 1
            
        return max_number
