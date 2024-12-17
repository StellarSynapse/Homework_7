def make_operation(operator, *args):
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
    else:
        raise ValueError("Invalid operator. Use '+', '-', or '*' only.")
    
    return result

# Example calls
print(make_operation('+', 7, 7, 2))  
print(make_operation('-', 5, 5, -10, -20)) 
print(make_operation('*', 7, 6))  
