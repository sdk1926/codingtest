# 빈 리스트에 하나씩 넣고 뒤에 숫자와 비교해서 들어있는 숫자가 작으면 뺀다. 
# 뺄때 k값을 1개씩 줄인다. 


def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while collected and k > 0 and collected[-1] < num:
            collected.pop()
            k -= 1 
        
        if k == 0:
            collected += number[i:]
            break
        
        collected.append(num)
    
    collected = collected[:-k] if k > 0 else collected 
    answer = "".join(collected)
    return answer