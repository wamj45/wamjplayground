import math, os

# ====== BitWise Operations ======
def xor(val1, val2):
    return (val1 ^ val2)

def and_op(val1, val2):
    return (val1 & val2)

def not_op(val1):
    ret = ""
    for bit in val1:
        chr = not int(bit)
        ret = ret + str(int(chr))
    return ret

def or_op(val1, val2):
    return (val1 | val2)

def nor_op(val1, val2):
    or_val = or_op(val1, val2)
    converted_bin = bin(or_val).replace("0b", "")
    return not_op(converted_bin)

def shr(val1, val2):
    try:
         ret = val1 >> val2
    except TypeError as err:
        print(f"Invalid operand for SHR entered!")
        print("Please consult operation manual for proper implementation of SHR!")
        os._exit(2)
    return ret

def shl(val1, val2):
    try:
        ret = val1 << val2
    except TypeError as err:
        print(f"Invalid operand for SHL entered!")
        print("Please consult operation manual for proper implementation of SHL!")
        os._exit(3)
    return ret


# ===== Math Operations ======
def multiply(val1, val2):
    return (val1 * val2)

def add(val1, val2):
    return (val1 + val2)

def sub(val1, val2):
    return (val1 - val2)

def div_op(val1, val2):
    return (val1 / val2)

# Testing Section
# input1 = 115
# input2 = 2143
# test_case = nor_op(input1, input2)
# print(f"[{input1}] NOR [{input2}] = [{test_case}]")
