# LINEAR SEARCH

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(arr[i])
            return i
arr = [2, 5, 8, 9, 10, 16, 22]
target = 10
print(search(arr, target))