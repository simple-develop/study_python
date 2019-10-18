
def convert_to_decimal(number, base):
    result_decimal = 0
    temp_mul = 1

    while number > 0:
        result_decimal += number % 10 * temp_mul
        number = number // 10
        temp_mul *= base
    return result_decimal

# use int
def convert_to_decimal2(number, base):
    return int(str(number), base)

if __name__ == "__main__":
    number = int(input("input number : "))
    base = int(input("input base : "))

    result_value = convert_to_decimal(number, base)
    result_value2 = convert_to_decimal2(number, base)

    print("result : {0}".format(result_value))
    print("result2 : {0}".format(result_value2))

