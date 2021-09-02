import sys
n = int(input())
for i in range(n):
    num, string = sys.stdin.readline().split()
    ans = [j * int(num) for j in string]
    print(''.join(ans))    