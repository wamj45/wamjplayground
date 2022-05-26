# Handler for SEM conversions
import convertor as convert

def get_dec(sem_input):
    sign_bit = int(sem_input[0])
    # remove the sign bit
    sem_input = sem_input[1:]
    exponent_portion = sem_input[0:9]
    mantissa_portion = sem_input[9:len(sem_input)]
    exp_factor = 7
    mantissa_factor = -2

    exponent = 0
    for exp_bit in exponent_portion:
        exponent = exponent + (int(exp_bit) * (2 ** exp_factor))
        exp_factor = exp_factor - 1

    mantissa = 0
    for mantissa_bit in mantissa_portion:
        mantissa = mantissa + (int(mantissa_bit) * (2 ** mantissa_factor))
        mantissa_factor = mantissa_factor - 1

    sign = (-1) ** (int(sign_bit))
    exponent = 2 ** (exponent - 127)
    mantissa = 1 + mantissa
    result = sign * exponent * mantissa
    return result

def get_sem_float(float_input):
    if float_input > 0:
        sign_bit = "0"
    else:
        sign_bit = "1"

    float_input = abs(float_input)
    exponent = "100000000"
    mantissa = ""
    whole, dec = str(float_input).split(".")
    whole = bin(int(whole)).replace("0b", "")+ "."
    dec = bin(int(dec)).replace("0b","")
    un_normalized = whole + dec
    exp = 0
    un_normalized = float(un_normalized)
    while True:
        if un_normalized / (10 ** exp) < 1:
            exp -= 1
            break
        exp += 1
    normalized = un_normalized / (10 ** exp)

    normalized_str = str(normalized)
    normalized_str = normalized_str[2:]

    em = exponent[0:len(exponent)-(exp)] + normalized_str
    em = em.ljust(31, "0")
    sem = sign_bit + em
    return sem
