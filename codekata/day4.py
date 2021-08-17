def same_reverse(num):
    # 아래 코드를 입력해주세요.
    reverse_num = list(str(num))
    reverse_num.reverse()
    num = list(str(num))
    if reverse_num == num:
      return True
    else:
      return False
   