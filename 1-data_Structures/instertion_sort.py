# python program to perform an insertion sort

# function to perform insertion sort on 1D array
def instertionSort(arr):

    #traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # move elements of arr[0,1....i-1] that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# test code
arr = [12, 11, 13, 5, 6]
instertionSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i])