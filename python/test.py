def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    tmp = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            tmp.append(left_arr[i])
            i+=1
        else:
            tmp.append(right_arr[j])
            j+=1
    tmp+=left_arr[i:]
    tmp+=right_arr[j:]
    return tmp

input = [3,4,5,2,1]
print(merge_sort(input))