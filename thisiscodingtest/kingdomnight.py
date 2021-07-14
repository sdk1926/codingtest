input_data = input()
row = int(input_data[1])
colum = int(ord(input_data[0]))-int(ord('a'))+1
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
count = 0 

for step in steps:
    new_row = row + step[0]
    new_colum = colum + step[1]
    if new_row >= 1 and new_row <= 8 and new_colum >= 1 and new_row <= 8:
        count += 1

print(count)

