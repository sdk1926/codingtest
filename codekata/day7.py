def more_than_half(nums):
    num_set=set(nums)
    len_num = len(nums)
    for i in num_set:
      if (len_num // 2)<= nums.count(i):
        return i 
      
