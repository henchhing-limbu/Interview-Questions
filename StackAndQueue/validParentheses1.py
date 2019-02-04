def validParentheses(s):
    parentheses = {
        ')': '('
        , '}':'{'
        , ']':'['
    }
    
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return "UNBALANCED"
            elif stack.pop() != parentheses[char]:
                return "UNBALANCED"
    return "BALANCED" if not stack else "UNBALANCED"
    
print(validParentheses(""))
