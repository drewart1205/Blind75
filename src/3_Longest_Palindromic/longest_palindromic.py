def longestPalindrome(self, s: str) -> str:
        n = len(s)
        pal_idx = [[False] * n for _ in range(n)]
        ans = s[0]
        for i in range(n):
            pal_idx[i][i] = True
        
        for end in range(n):
            for start in range(end):
                string = s[start:end+1]
                if s[start]==s[end] and (pal_idx[start+1][end-1] or end==start + 1):
                    pal_idx[start][end] = True
                    if len(string) > len(ans):
                        ans = string
        
        return ans