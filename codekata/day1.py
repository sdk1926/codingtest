def two_sum(nums, target):
    # 아래 코드를 작성해주세요.
    dic = {i:v for v, i in enumerate(nums)}
    result = []
    for i in nums:
      tmp = target - i
      if tmp in dic:
        result.append(dic[i])
        result.append(dic[tmp])
        break
    return result
        
