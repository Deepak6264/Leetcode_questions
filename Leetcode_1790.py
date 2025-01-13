class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        li = []
        for i in range(n):
            if(s1[i] != s2[i]):
                li.append(i)
        if(len(li) == 0):
            return True
        if(len(li) == 2):
            return s1[li[0]] == s2[li[1]] and    s1[li[1]] == s2[li[0]]
        return False;              


        
