a =  "Mazatneunde Wae Teullyeoyo"
b = a.split(' ')
try:
    while True:
        b.remove('')
        if '' not in b:
            break
except:
    print(b)
    print(len(b))
else:
    print(b)
    print(len(b))