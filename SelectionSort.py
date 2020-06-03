'''Loop array and move the smallest number to the front in every iteration
Time Complexity - O(n^2)
Space Complexity - O(1)
'''

def selectionSort(arr):
    for i in range(len(arr) - 1):
        tempSmall = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[tempSmall]:
                tempSmall = j
        tempSmallValue = arr[tempSmall]
        arr[tempSmall] = arr[i]
        arr[i] = tempSmallValue
    print(arr)

items = [14, 4, 1, 65, 34, 6]
selectionSort(items)
