class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0
        for a in words:
            if len(a) >= n:
                for i in range(n):
                    if a[i] != pref[i]:
                        break
                    elif i+1 == n:
                        count += 1    
                # substr=  a[:n]
                # if pref == substr:
                #     count += 1 
        return count            
        
