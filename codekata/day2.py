def reverse(number):
  # 여기에 코드를 작성해주세요.
  num = -1
  if number < 0:
    number *= num
    number = int(''.join((list(str(number))[::-1])))
    number *= num
    return number
  number = int(''.join((list(str(number))[::-1])))
  return number  

    