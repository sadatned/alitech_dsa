import time

def print_stack(stack):
    print("\nCurrent Stack (top -> bottom):")
    for element in reversed(stack):
        print(f"| {element} |")
    print(" ----- ")
    time.sleep(1)  # Adding a delay to visualize the steps clearly

def push(stack, element):
    print(f"\nPushing {element} onto the stack...")
    stack.append(element)
    print_stack(stack)

def pop(stack):
    if not stack:
        print("\nThe stack is empty. Cannot pop!")
        return
    print(f"\nPopping {stack[-1]} from the stack...")
    stack.pop()
    print_stack(stack)

def peek(stack):
    if not stack:
        print("\nThe stack is empty. Nothing to peek.")
        return
    print(f"\nThe top element is {stack[-1]}")
    print_stack(stack)

def is_empty(stack):
    if not stack:
        print("\nThe stack is currently empty.")
    else:
        print("\nThe stack is not empty.")
    print_stack(stack)

def main():
    print("Welcome to the interactive Stack Operations program!")
    time.sleep(1)
    
    # Initialize an empty stack
    stack = []
    print("\nStarting with an empty stack.")
    print_stack(stack)
    
    # Push elements
    push(stack, 10)
    push(stack, 20)
    push(stack, 30)
    
    # Peek at the top element
    peek(stack)
    
    # Pop elements
    pop(stack)
    pop(stack)
    
    # Check if the stack is empty
    is_empty(stack)
    
    # Pop the last element
    pop(stack)
    
    # Check if the stack is empty again
    is_empty(stack)

if __name__ == "__main__":
    print("Self-Explanatory Python Program: Stack Operations")
    print("===================================================")
    main()
