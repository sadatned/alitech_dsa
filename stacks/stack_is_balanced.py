'''
Checking for Balanced Parentheses
Stacks are widely used to check if parentheses (or other delimiters) in an expression are balanced.
'''
def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
            print(f"Pushed {char} onto the stack.")
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                print(f"Unbalanced at character {char}")
                return False
            print(f"Popped matching opening brace for {char}")
    if stack:
        print("Unbalanced - Stack is not empty at the end.")
        return False
    return True

expr = "{[()()]}"
print(f"Expression '{expr}' is balanced: {is_balanced(expr)}")
