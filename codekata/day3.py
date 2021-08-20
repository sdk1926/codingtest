def get_len_of_str(s):
    # 아래 코드를 작성해주세요.
    dic = {}
    long = 0 
    for i, v in enumerate(s):
      if v in dic and len(dic) > long:
          long = len(dic)
          dic.clear()
          dic[v] = i
      else:
        dic[v] = i
    return  max(long, len(dic))





