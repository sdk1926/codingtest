from typing import * 

# 내풀이 -> 시간초과
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = deque(temperatures)
        answer = []
        for i in range(len(temperatures)):
            a = temperatures.popleft()
            while True:
                j = 0 
                if temperatures[j] <= a:
                    j += 1
                elif temperatures[j] > a:
                    j += 1
                    answer.append(a)
                    break 
                if j >= len(temperatures):
                    answer.append(0)
                    break

 # 상길 선생님의 풀이
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:                    
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리 
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer 