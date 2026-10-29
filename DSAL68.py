queue = []
SIZE = 5

def enqueue(x):
    if len(queue) == SIZE:
        print("Queue Overflow")
    else:
        queue.append(x)
        print(x, "inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print(queue.pop(0), "removed")

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)

while True:
    print("1. Enqueue ")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue(int(input("Enter value: ")))
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")

