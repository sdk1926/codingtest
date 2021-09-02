string = input().upper()
compare = set(string)
ans = [(string.count(value), value)for value in compare]
ans = sorted(ans, reverse=True)
if len(ans) > 1 and ans[0][0] == ans[1][0]: print("?")
else: print(ans[0][1])