n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())    
    people = [i for i in range(1, n+1)]
    for j in range(k):
        for m in range(1,n):
            people[m] += people[m-1]
    print(people[-1])