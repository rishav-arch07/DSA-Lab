# Linear Search Program

a = [10 ,20 ,30 , 40, 50]
x = int(input("Enter element to search:"))

for i in range(len(a)):
    if a[i]==x:
        print("Enter found at index",i)
        break
    else: 
        print("Element not found")
         