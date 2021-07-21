import sys
n = int(sys.stdin.readline())
list1 = list(map(int,sys.stdin.readline().split(' ')))
list1.sort()
m = int(sys.stdin.readline())
list2 = list(map(int,sys.stdin.readline().split(' ')))

def bisearch(key):
    start=0
    end= n-1
    while start <= end:
        mid=(start+end)//2
        if list1[mid]==key:
            return True
        elif list1[mid] < key:
            start=mid +1
        else:
            end=mid -1

for l in range(m):
    if bisearch(list2[l]):
        print(1)
    else:
        print(0)
