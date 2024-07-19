def valid_braces(string):
    braces = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>'
    }
    stack= []
    
    for char in string:
        if char in braces:
                stack.append(char)
        elif len(stack) == 0 or braces[stack.pop()] != char:
            return False
    return len(stack) ==  0           


print(valid_braces('{<{}>}'))