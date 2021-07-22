n = int(input())
order = []
for _ in range(n):
    order.append(list(input().split(' ')))

class Stack():
    def __init__(self):
        self.array = []

    def push(self,num):
        self.array.append(num)


    def popin(self):
        if self.array:
            a = self.array.pop()
            print(a)
        else:
            print(-1)

    def size(self):
        print(len(self.array))

    def empty(self):
        if self.array:
            print(0)
        else:
            print(1)

    def top(self):
        if self.array:
            print(self.array[-1])
        else:
            print(-1)

ak = Stack()

for i in range(n):
    if order[i][0] == 'push':
        ak.push(int(order[i][1]))
    elif order[i][0] == 'pop':
        ak.popin()
    elif order[i][0] == 'size':
        ak.size()
    elif order[i][0] == 'empty':
        ak.empty()
    elif order[i][0] == 'top':
        ak.top()