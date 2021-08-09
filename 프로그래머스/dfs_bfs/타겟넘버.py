# bfs 
def solution(numbers, target):
    result = [0]
    for i in range(len(numbers)):
        result_list = []
        for j in range(len(result)):
            result_list.append(result[j]+numbers[i])
            result_list.append(result[j]-numbers[i])
        result = result_list
    answer = result.count(target)
    return answer

# dfs 
def solution(numbers, target):
    answer = 0 
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])
    dfs(0,0)
    
    return answer