def quicksort(arr):
    if len(arr) < 1:  
        return arr
    else:
        pivot = arr[len(arr)-1]
        smaller = [i for i in arr[:len(arr)-1] if i <= pivot]  
        greater = [i for i in arr[:len(arr)-1] if i > pivot]   
        return quicksort(smaller) + [pivot] + quicksort(greater)  

arr = [1,3,2,4]
sorted_arr = quicksort(arr)
print(sorted_arr)
