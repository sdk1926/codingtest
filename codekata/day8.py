def is_valid(string):
    arr = []
    stack = {
      ')':'(',
      ']':'[',
      '}':'{'
    }
    for i in string:
      if arr and i in stack and stack[i] in arr:
        arr.pop()
      else:  
        arr.append(i)
    return len(arr) == 0
