s = "cbacdcbc"
s = list(s)
list1 = []
for _ in range(len(s)):
    a = s.pop(0)
    if a not in s:
        list1.append(a)
print(list1)