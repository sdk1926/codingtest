# 내 풀이 

def top_k(nums, k):
    # 여기에 코드를 입력해주세요
    list1 = dict()
    nums2 = set(nums)
    ans = []
    for i in nums2:
      list1[nums.count(i)] = i
    sdict = sorted(list1.items(), reverse=True)
    print(sdict)
    for i in range(k):
      ans.append(sdict[i][1])
    return ans