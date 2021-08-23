# 상길선생님의 풀이 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'['            
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or stack.pop() != table[char]:
                return False 
        return len(stack) == 0
        