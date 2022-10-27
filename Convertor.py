ALLOWED_OPERATORS = {"+", "-", "/", "*"}


def roman_to_int(s):
    rom_val = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val


def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def calculator(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '/':
        return number1 / number2
    elif operation == '*':
        return number1 * number2
    else:
        raise ValueError("invalid operator")


def calculate_result(numbers, operations):
    total = numbers[0]
    for i in range(1, len(numbers)):
        total = calculator(total, numbers[i], operations[i - 1])

    return total


def main():
    numbers = list()
    operators = list()

    is_input_number = True
    while True:
        if is_input_number:
            input_string = input("Please insert the number: ")
            if input_string == "exit":
                is_input_number = True
            else:
                # TODO check if input string is correct
                numbers.append(input_string)
                is_input_number = False
        else:
            input_string = input("Please insert the operator: ")
            if input_string == "exit":
                is_input_number = False
            else:
                if input_string in ALLOWED_OPERATORS:
                    operators.append(input_string)
                    is_input_number = True
                else:
                    print("operation not allowed")
                    continue
        # check if exit is needed and the last action was number input not operator
        if input_string == "exit":
            if is_input_number:
                print("Please insert the number first as the total operation is not correct")
                continue
            else:
                break

    # transfer to roman
    numbers = [roman_to_int(number) for number in numbers]
    # int
    total = calculate_result(numbers, operators)
    # roman
    total = int_to_roman(total)

    return total


result = main()
print(result)
