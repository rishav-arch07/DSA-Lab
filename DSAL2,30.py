      #write a program to impement a binary search algorithm to find an item in a sorted array.

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter sorted elements: ").split()))
x = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2 

    if arr[mid] == x:
        print("Element found at position", mid + 1)
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")