cro = {'c=':2,'c-':1,'dz=':3,'d-':2,'lj':2,'nj':2,'s=':2,'z=':2}
word = input()
ans = 0
i = 0
while True:
    if word[i:i+3] in cro:
        i += 3
        ans += 1
    elif word[i:i+2] in cro:
        i += 2
        ans += 1
    else:
        i += 1
        ans += 1
    if i == len(word)-1:
        ans +=1
        break
    elif i >= len(word):
        break
print(ans)