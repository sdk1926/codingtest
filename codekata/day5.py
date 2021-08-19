# 짝꿍풀이

def get_prefix(strs):
    if not strs:
        return ''
    min_len = len(min(strs, key=len))
    arr = []
    for i in range(min_len):
        tmp = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != tmp:
                return ''.join(arr)
        arr.append(tmp)
    return ''.join(arr)

# 내 풀이 
def get_prefix(strs):
    if not strs:
      return ''
    strs.reverse()
    num = strs.pop(0)
    num_len = len(num)
    results = ''
    results2 = [0]* num_len
    for i in range(num_len):
      compare_num = num[i]
      for j in strs:
        if j[i] == compare_num:
          results2[i] = 1
        else:
          results2[i] = 0
          break 
      if results2[i] == 0:
        break  
    count_num = results2.count(1)
    if count_num == 0:
      return results
    else:
      results = num[:count_num]
      return results
        
