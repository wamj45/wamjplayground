
# Should recieve a dec val and convert to the various values

def float_convert(value):
    return float(value)

def hex_convert(value):
    return hex(value)

def float_hex(value):
    return float.hex(value)

def bin_convert(dec_value):
    return bin(dec_value).replace("0b", "")

def float_bin(float_value):
    def dec_conversion(num):
        while num > 1:
            num /= 10
        return num

    whole, dec = str(float_value).split(".")
    whole = int(whole)
    if len(dec) > 1:
        if dec[0] == "0":
            dec = dec[1:]
    dec = int(float(dec))

    ret = bin_convert(whole) + "."
    if dec == 0:
        return ret + "0"
    for i in range(8):
        if dec == 0:
            break
        whole, dec = str((dec_conversion(dec)) * 2).split(".")
        dec = int(dec)
        ret += whole
    return ret

def dec_convert(value, format):
    return int(value, format)


# test_case = 31.25
# print(float_bin(test_case))
