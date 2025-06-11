#Calculator function

def safe_divide(numerator, denominator):
    '''Safe division while handling errors'''
    try:
        result = float(numerator) / float(denominator)
        return f'The result of the division is {result}'
    
    #catch zero division
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    #catch invalid values
    except ValueError:
        return 'Error: Please enter numeric values only.'