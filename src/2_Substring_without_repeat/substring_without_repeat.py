ef lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        s_len = len(s)
        seen = {}

        length = 0

        for i in range(s_len):
            length = 1
            seen[s[i]] = True
            for j in range(i+1, s_len):
                if s[j] in seen: 
                    if length > max_length:
                        max_length = length
                    seen = {}
                    break
                else:
                    length += 1
                    seen[s[j]] = True
                
        if length > max_length:
            max_length = length
        
        return max_length