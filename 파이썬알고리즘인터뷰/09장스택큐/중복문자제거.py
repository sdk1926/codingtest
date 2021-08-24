# 상길선생님 스택 풀이 
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        
        return ''.join(stack)

# 재귀 풀이 (인간의 머리로 이해불가) 
class solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 정렬 
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일피할 때 분리 진행 
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''