input_number = int(input("Please enter an input: "))
result = []


def decimal_to_binary(num, rem):

    if num > 1:
        decimal_to_binary(num // 2, rem)
    rem.append(num % 2)


decimal_to_binary(input_number, result)


print(result)
