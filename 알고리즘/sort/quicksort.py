def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end 
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] =  array[right], array[left]
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

arr = [3,5,6,3,4,65,7,3,1,5,54,7,4]

quick_sort(arr,0,len(arr)-1)
print(arr)

def pythonic_quicksort(array):
    
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return pythonic_quicksort(left_side) + [pivot] + pythonic_quicksort(right_side)

print(pythonic_quicksort(arr))