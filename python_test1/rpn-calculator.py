from math import sqrt


def calc_expressions(input_list, pos):
    operator = input_list[pos]
    list_rest = input_list[pos + 1:]
    num_one = input_list[pos - 2]
    num_two = input_list[pos - 1]

    if operator == '+':
        list_first = input_list[:pos - 2]
        list_sum = [float(num_one) + float(num_two)]
        return list(list_first + list_sum + list_rest)
    elif operator == '*':
        list_first = input_list[:pos - 2]
        list_sum = [float(num_one) * float(num_two)]
        return list(list_first + list_sum + list_rest)
    elif operator == '-':
        list_first = input_list[:pos - 2]
        list_sum = [float(num_one) - float(num_two)]
        return list(list_first + list_sum + list_rest)
    elif operator == '/':
        list_first = input_list[:pos - 2]
        list_sum = [float(num_one) / float(num_two)]
        return list(list_first + list_sum + list_rest)
    elif operator == 'sqrt':
        list_first = input_list[:pos - 1]
        list_sum = [sqrt(num_two)]
        return list(list_first + list_sum + list_rest)        

    return list()


def supported_expressions(element):
    if element == '+' or element == '-' or element == '*' or element == '/' or element == 'sqrt':
        return True

    return False


def rpn_calc(str_exp):
    result = 0
    num_and_op = str_exp.split(' ')

    while True:
        if len(num_and_op) == 1:
            result = num_and_op[0]
            break

        for pos, element in enumerate(num_and_op):
            if supported_expressions(element):
                num_and_op = calc_expressions(num_and_op, pos)
                break

    return result


print(rpn_calc('6 8 4 + 3 2 + - *'))
print(rpn_calc('3 4 2 + *'))
print(rpn_calc('5 4 2 * 3 + + sqrt'))
print(rpn_calc('3.12 4 + 2 *'))
