from parsing_exception import ParsingException


def parse_string_with_exception(x):
    try:
        return parse_string(x)
    except:
        raise ParsingException('Error while parsing the string or calc')


def parse_string(x):
    operators = set('+-*/')
    pos_neg_signs = set('+-')

    op_out = []  # holds the operators that are found in the string (left to right)
    num_out = []  # holds the non-operators that are found in the string (left to right)

    next_expected = 'O1|N1'

    buff = []
    sign = None

    for c in x:
        if next_expected == 'O1|N1':
            if c in pos_neg_signs:
                sign = c
                next_expected = 'N1'
            else:
                next_expected = 'N1'
                buff.append(c)
        else:
            if c in operators:

                if next_expected == 'N1' and sign == '-':
                    buff.insert(0, '-')

                num_out.append(to_number(buff))

                buff = []
                op_out.append(c)
                next_expected = 'N2'
            else:
                buff.append(c)

    if len(buff) > 0:
        num_out.append(to_number(buff))

    result = num_out + op_out
    return result


def to_number(buff):
    number = ''.join(buff)
    casted_number = float(number)
    return casted_number
