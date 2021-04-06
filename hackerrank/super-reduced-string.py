from collections import deque

# Complete the superReducedString function below.
def superReducedString(s):
    stack = deque()
    
    for char in s:
        if not stack:
            stack.append(char)
        elif char == stack[-1]:
            stack.remove(char)
        else:
            stack.append(char)
            
    result = get_reduced_string(stack)
    
    if not result:
        return "Empty String"
    else:
        return result
    
def get_reduced_string(stack):
    string = ''
    
    for char in stack:
        string += char
        
    return string

print(superReducedString('mwkommokwmxjivkkvijxshscbbcshsgwdyqqydwgzpnlzzlnpzvfeaiiaefvyeqjccjqeymhqhiihqhmhaomkkmoahhddymmyddh'))

