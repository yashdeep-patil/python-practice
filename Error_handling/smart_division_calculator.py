def smart_division(a, b):

    try:
        result = a/b

    except ZeroDivisionError: 
        return "You can't divide by zero"

    except TypeError:
        return "Please provide numbers only"   
    
    else:
        return result
print(smart_division(10, 2))
print(smart_division(10, 0))    
print(smart_division("adc", 10))    