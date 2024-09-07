def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
