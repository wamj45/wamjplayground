import re, os
import convertor as convert
import sem_converter as sem_convert

# Regular Expressions for inputs
HEX_REG_EX = "^0x[0-9a-fA-F]+$"
BIN_REG_EX = "^[0-1]+$"
FLOAT_POINT_REG_EX  = "^[-+]?[0-9]+\.[0-9]+$"
SEM_REG_EX = "^(0|1){32}$"
INT_REG_EX = "^[0-9]+$"

class InputHandler:
    def __init__(self):
        self.input_type     = None
        self.input_value    = None
        self.dec_input      = None
        self.sem            = None
        self.floating_pt    = None
        self.hexadecimal    = None
        self.binary         = None
        self.shift_bits     = None

    def set_input(self, value):
        self.input_value = value

    def get_input(self):
        user_input = str(input("Please enter a number: "))
        self.set_input(user_input)

    def clear(self):
        self.input_type     = None
        self.input_value    = None
        self.dec_input      = None
        self.sem            = None
        self.floating_pt    = None
        self.hexadecimal    = None
        self.binary         = None
        self.shift_bits     = None

    def run(self):
        if self.initialize() is False:
            print("Error - Failed to initialize Convertor App")
            return False

        if self.populate_values() is False:
            print("Error - Failed to convert input!")
            return False
        self.display_output()
        print("Exiting AtomicRobotLemur Converter App!")
        return True

    def initialize(self):
        if self.input_value is not None:
            self.clear()

        self.get_input()
        self.input_type = self.identify_input(self.input_value)
        if self.input_type is None:
            print("Unaccepted Input entered! Please enter a valid input")
            os._exit(255)
            return False
        return True

    def identify_input(self, input):
        if re.fullmatch(HEX_REG_EX, input) is not None:
            self.hexadecimal = input
            return "hexadecimal"
        elif re.fullmatch(SEM_REG_EX, input) is not None:
            self.sem = input
            return "SEM"
        elif re.fullmatch(BIN_REG_EX, input) is not None:
            self.binary = input
            return "binary"
        elif re.fullmatch(FLOAT_POINT_REG_EX, input) is not None:
            self.floating_pt = input
            return "float"
        elif re.fullmatch(INT_REG_EX, input) is not None:
            self.shift_bits = int(input)
            return "int"
        return None

    def populate_values(self):
        if self.hexadecimal is not None:
            self.dec_input = convert.dec_convert(self.hexadecimal, 16)
            self.binary = convert.bin_convert(self.dec_input)
            self.floating_pt = convert.float_convert(self.dec_input)
            self.sem = sem_convert.get_sem_float(self.floating_pt)
        elif self.binary is not None:
            self.dec_input = convert.dec_convert(self.binary, 2)
            self.floating_pt = convert.float_convert(self.dec_input)
            self.hexadecimal = convert.hex_convert(self.dec_input)
            self.sem = sem_convert.get_sem_float(self.floating_pt)
        elif self.floating_pt is not None:
            # convert from float to the other values
            self.dec_input = float(self.floating_pt)
            self.hexadecimal = convert.float_hex(self.dec_input)
            self.binary = convert.float_bin(self.dec_input)
            self.sem = sem_convert.get_sem_float(self.dec_input)
        elif self.sem is not None:
            # convert from sem to the other values
            self.dec_input = sem_convert.get_dec(self.sem)
            self.floating_pt = convert.float_convert(self.dec_input)
            self.hexadecimal = convert.float_hex(self.floating_pt)
            self.binary = convert.float_bin(self.floating_pt)
        else:
            return False
        return True


    def display_output(self):
        print("\n-------------------------------------------------------------------------------")
        print(f"Given: {self.input_value}\n")
        print(f"HEX: {self.hexadecimal} | BINARY: {self.binary} | FLOAT: {self.floating_pt} | SEM: {self.sem}")
        print("-------------------------------------------------------------------------------\n")
        return

# def main():
#     handler = InputHandler()
#     if handler.run() is False:
#         os._exit(1)
#
# if __name__ == '__main__':
#     main()
