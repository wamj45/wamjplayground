# should recieve two inputs and an operator.
# At the same time should be able to display the convertered output
import math_op
import convertor
import sem_converter
from single_input_handler import InputHandler
from enum import Enum
import os

OPERATOR_STRING = "Allowable operations:\n1.  Addition\n2.  Subtraction\n3.  Multiplication\n4.  Division\n5.  AND\n6.  NOT\n7.  OR\n8.  NOR\n9.  XOR\n10. SHR\n11. SHL\n"

class Operator(Enum):
    ADDITION        = 1
    SUBTRACTION     = 2
    MULTIPLICATION  = 3
    DIVISION        = 4
    AND             = 5
    NOT             = 6
    OR              = 7
    NOR             = 8
    XOR             = 9
    SHR             = 10
    SHL             = 11

class Calculator:
    def __init__(self):
        self.input1     = InputHandler()
        self.input2     = InputHandler()
        self.operator   = None
        self.op_type    = None
        self.result     = None

    def run(self):
        print("\nWelcome to the Calculator App!")
        try:
            self.input1.run()
            self.input2.run()
            print(OPERATOR_STRING)
            self.operator = int(input("Please enter an operator option: "))
        except Exception as e:
            print("Error - Failed to handle inputs")
            print(f"{str(e)}")
            return False
        self.result = self.evaluate_calculation()
        self.display_output()
        return True

    def result_output(self):
        hex_ans = convertor.hex_convert(self.result)
        binary_ans = convertor.bin_convert(self.result)
        fp_ans = convertor.float_convert(self.result)
        sem_ans = sem_converter.get_sem_float(fp_ans)

        print("\n-------------------------------------------------------------------------------")
        print(f"{self.input1.input_value} {self.op_type} {self.input2.input_value} =")
        print(f"HEX: {hex_ans} | BINARY: {binary_ans} | FLOAT: {fp_ans} | SEM: {sem_ans}")
        print("-------------------------------------------------------------------------------\n")
        return

    def float_output(self):
        hex_ans = convertor.float_hex(self.result)
        binary_ans = convertor.float_bin(self.result)
        fp_ans = convertor.float_convert(self.result)
        sem_ans = sem_converter.get_sem_float(self.result)

        print("\n-------------------------------------------------------------------------------")
        print(f"{self.input1.input_value} {self.op_type} {self.input2.input_value} =")
        print(f"HEX: {hex_ans} | BINARY: {binary_ans} | FLOAT: {fp_ans} | SEM: {sem_ans}")
        print("-------------------------------------------------------------------------------\n")
        return

    def display_output(self):
        if isinstance(self.result, float) is True:
            self.float_output()
        else:
            self.result_output()

        choice = ""
        while choice != "0":
            choice = input("Enter (1) to see first input conversion values\nEnter (2) to see second input conversion values\nEnter (3) to see results conversions\nEnter (0) to exit\n")

            if choice == "1":
                self.input1.display_output()
            elif choice == "2":
                self.input2.display_output()
            elif choice == "3":
                if isinstance(self.result, float) is True:
                    self.float_output()
                else:
                    self.result_output()
        print("Exiting AtomicRobotLemur Calculator!")
        os._exit(0)
        return

    def evaluate_calculation(self):
        if self.operator == Operator.ADDITION.value:
            self.op_type = "+"
            return math_op.add(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.SUBTRACTION.value:
            self.op_type = "-"
            return math_op.sub(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.MULTIPLICATION.value:
            self.op_type = "*"
            return math_op.multiply(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.DIVISION.value:
            self.op_type = "/"
            return math_op.div_op(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.AND.value:
            self.op_type = "&"
            return math_op.and_op(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.NOT.value:
            self.op_type = "~"
            return math_op.not_op(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.NOR.value:
            self.op_type = "NOR"
            nor_ans = math_op.nor_op(self.input1.dec_input, self.input2.dec_input)
            return convertor.dec_convert(nor_ans, 2)
        elif self.operator == Operator.OR.value:
            self.op_type = "|"
            return math_op.or_op(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.XOR.value:
            self.op_type = "^"
            return math_op.xor(self.input1.dec_input, self.input2.dec_input)
        elif self.operator == Operator.SHL.value:
            self.op_type = "<<"
            return math_op.shl(self.input1.dec_input, self.input2.shift_bits)
        elif self.operator == Operator.SHR.value:
            self.op_type = ">>"
            return math_op.shr(self.input1.dec_input, self.input2.shift_bits)
        else:
            print("\nInvalid Operation selected! Closing App...")
            os._exit(1)
