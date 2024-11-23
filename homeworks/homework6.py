def binary_sort(arr, num):
    pos = 0
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if num == arr[mid]:
            pos = mid
            print('Элемент найден на позиции ', pos)
            return pos
        elif num > arr[mid]:
            first = mid + 1
        elif num < arr[mid]:
            last = mid - 1
    
    print('Элемент не найден')

            
print(binary_sort([1,2,3,4,5,6,7,8,9,10], 7))



def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(bubble_sort([1,0,5,4,8,1,10]))