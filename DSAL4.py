class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [0] * size

   
    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return

        self.top += 1
        self.arr[self.top] = value

   
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return

        self.top -= 1

   
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return

        print("The peek element is =", self.arr[self.top])


s = Stack(3)

while True:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
