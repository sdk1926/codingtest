import sys
import math

a,b,c = map(int,input().split())
d = c - a
print(math.ceil(d / (a-b))+1)
