# write a program to read a linear list of items and store it in an array. 

n = int(input("Enter a number of the items:"))
arr = []
print("Enter the items:")
for i in range(n):
    item = input()
    arr.append(item)
print("The items stored in the list are:")
print(arr)