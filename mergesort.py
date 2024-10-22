def mergeSort(array):

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    leftDivided = mergeSort(left)
    rightDivided = mergeSort(right)

    return merge(leftDivided, rightDivided)

def merge(left,right):
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+= 1
        else:
            merged.append(right[j])
            j += 1
        
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

array = [8,3,2,9,7,5,1,4,6,0]
sortedArray = mergeSort(array)

print(sortedArray)