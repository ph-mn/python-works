''' Bubbling bigger number to end of the list
Repeat this untill array sorted'''

items = [30, 23, 7, 12, 4, 13]
for i in range(len(items)):
    for j in range(len(items) - 1 - i):
        if items[j] > items[j+1]:
            temp = items[j]
            items[j] = items[j+1]
            items[j+1] = temp

print(str(items))

#Time Complexity - O(n^2)
