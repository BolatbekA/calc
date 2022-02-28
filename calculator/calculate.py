def calculate(tokens):
    operators = {'+': op_plus,
                 '-': op_minus,
                 '*': op_multiply,
                 '/': op_divide}

    stack = []
    for token in tokens:
        if token in operators:
            operators[token](stack)
        else:
            stack.append(token)

    calculated = stack[0]
    result = int(calculated) if calculated.is_integer() else round(calculated, 3)

    return result


def get_operands(stack):
    return stack.pop(0), stack.pop(0)


def op_plus(stack):
    x, y = get_operands(stack)
    stack.append(x + y)


def op_minus(stack):
    x, y = get_operands(stack)
    stack.append(x - y)


def op_multiply(stack):
    x, y = get_operands(stack)
    stack.append(x * y)


def op_divide(stack):
    x, y = get_operands(stack)
    stack.append(x / y)
