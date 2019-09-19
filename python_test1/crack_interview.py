'''
    is string unique?
'''


def has_unique_char(characters):
    if len(characters) > 256:
        return False

    chart_set = [0] * 256

    for pos in range(len(characters)):
        val = ord(characters[pos])
        if chart_set[val]:
            return False

        chart_set[val] = True

    return True

print(has_unique_char('abcdz'))
print('********************* Unique String *********************************')


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string
def say_hi():
    return 'hello there'

print(say_hi())

x = ['ab', 'cd']
print((list(map(list, x))))

n = [2, 3, 4]
print(sum(n))


def reverse_num(num):
    result, abs_num = 0, abs(num)
    while abs_num:
        result = result * 10 + (abs_num % 10)
        abs_num //= 10

    return result if num > 0 else -result

print(reverse_num(-1234))


def
