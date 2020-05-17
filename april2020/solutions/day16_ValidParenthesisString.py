# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid.
# We define the validity of a string by these rules:

# 1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# 5. An empty string is also valid.

# Example 1:
# Input: "()"
# Output: True

# Example 2:
# Input: "(*)"
# Output: True

# Example 3:
# Input: "(*))"
# Output: True

def checkValidString(s):
    openStack = []
    starStack = []
    for i in range(len(s)):
        if s[i] == "(":
            openStack.append(i)
        elif s[i] == "*":
            starStack.append(i)
        else:
            if openStack:
                openStack.pop()
            elif starStack:
                starStack.pop()
            else:
                return False
    while openStack and starStack:
        if not openStack.pop() < starStack.pop():
            return False
    return len(openStack)==0
