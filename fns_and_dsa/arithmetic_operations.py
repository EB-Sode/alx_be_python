def perform_operation(num1, num2, operation):
        match operation:
            case 'add':
                return num1 + num2
            case 'subtract':
                return num1 - num2
            case 'multiply':
                return num1 * num2
            case 'divide':
                if num2 == 0: 
                    return "num2 cannot be zero for division."
                elif num1 == 0:
                    return num1 / num2
                else:
                    return num1 / num2
            case _:
                return "Invalid operation. Please choose from add, subtract, multiply, or divide."



