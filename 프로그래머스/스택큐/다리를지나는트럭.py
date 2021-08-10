trucks = [7,4,5,6]
length = 2
weight = 10

i = 0
j = 0
도로 = []
a = trucks[0]

while trucks or 도로: 

    def 채워주기(도로):
        global length
        while len(도로)+1 <= length and sum(도로)+a <= weight:
            도로.append(a)
            print(도로)
            trucks.pop(0)
            print(trucks)

        return 도로 
    
    채워주기(도로)
    도로.pop(0)
    length += 1 











