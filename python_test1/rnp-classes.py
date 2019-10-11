class RPNExpresion(object):

    def __init__(self, operation):
        self.operation = operation

    def exec_operation(stack):
        pass


class RPNSum(RPNExpresion):

    def __init__(self):
        super().__init__('+')

    def exec_operation(stack):

        return stack.push(float(stack.pop()) + float(stack.pop()))


class RPNRest(RPNExpresion):

    def __init__(self):
        super().__init__('-')

    def exec_operation(stack):
        return stack.push(float(stack.pop()) - float(stack.pop()))


def supported_expressions(element):
    if element == '+' or element == '-' or element == '*' or element == '/' or element == 'sqrt':
        return True

    return False


def rpn_calc(str_exp):
    result = 0
    num_and_op = str_exp.split(' ')
    stack = []

    for element in num_and_op:
        if not supported_expressions(element):
            stack.push(element)
        else:
            

  

    while True:
        if len(num_and_op) == 1:
            result = num_and_op[0]
            break

        for pos, element in enumerate(num_and_op):
            if supported_expressions(element):
                num_and_op = calc_expressions(num_and_op, pos)
                break

    return result

test = RPNSum()
print(test.exec_operation())
