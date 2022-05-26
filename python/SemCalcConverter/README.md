# Atomic Robot Lemurs

## SWEN 4342 Spring 2022


### Usage
#### Running in a UNIX Terminal:
To run the program type ```python3 app.py```. Enter one or two inputs. To exit type ```Ctrl+C```


#### Input Format
All Hex numbers MUST be prefixed with ```0x``` such as
```
0x19AC 0x8A12 0xFFFFFFF
```
All SEM inputs must be of the following format:
```
11000000000101100000000000000000 01010000000101100000000000000000
```

For `SHR` and `SHL` user must enter an `integer` for the second value in order for shift to work

```
input1: 101010
input2: 2
operator: SHR
```


#### Calculator Operation Selection
Operator selection done by entering option number. To select ```Addition``` enter ```1```. Follow same procedure for the other operations


# Examples
## Converter
```
Do you wish to use the convertor or calculator?
Please enter 1 for the convertor, 2 for the calculator, or 0 to exit
1
Please enter a number: 0x19ac

-------------------------------------------------------------------------------
Given: 0x19ac

HEX: 0x19ac | BINARY: 1100110101100 | FLOAT: 6572.0 | SEM: 01000001001101011000000000000000
-------------------------------------------------------------------------------

Exiting AtomicRobotLemur Converter App!
```
## Calculator
Addition
```
Do you wish to use the convertor or calculator?
Please enter 1 for the convertor, 2 for the calculator, or 0 to exit
2    

Welcome to the Calculator App!
Please enter a number: 10101

-------------------------------------------------------------------------------
Given: 10101

HEX: 0x15 | BINARY: 10101 | FLOAT: 21.0 | SEM: 01000001010000000000000000000000
-------------------------------------------------------------------------------

Please enter a number: 1010

-------------------------------------------------------------------------------
Given: 1010

HEX: 0xa | BINARY: 1010 | FLOAT: 10.0 | SEM: 01000000100000000000000000000000
-------------------------------------------------------------------------------

Allowable operations:
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  AND
6.  NOT
7.  OR
8.  NOR
9.  XOR
10. SHR
11. SHL

Please enter an operator option: 1

-------------------------------------------------------------------------------
10101 + 1010 =
HEX: 0x1f | BINARY: 11111 | FLOAT: 31.0 | SEM: 01000011110000000000000000000000
-------------------------------------------------------------------------------

Enter (1) to see first input conversion values
Enter (2) to see second input conversion values
Enter (3) to see results conversions
Enter (0) to exit
```
Multiplication
```
Do you wish to use the convertor or calculator?
Please enter 1 for the convertor, 2 for the calculator, or 0 to exit
2

Welcome to the Calculator App!
Please enter a number: 10101

-------------------------------------------------------------------------------
Given: 10101

HEX: 0x15 | BINARY: 10101 | FLOAT: 21.0 | SEM: 01000001010000000000000000000000
-------------------------------------------------------------------------------

Please enter a number: 0x19ac

-------------------------------------------------------------------------------
Given: 0x19ac

HEX: 0x19ac | BINARY: 1100110101100 | FLOAT: 6572.0 | SEM: 01000001001101011000000000000000
-------------------------------------------------------------------------------

Allowable operations:
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  AND
6.  NOT
7.  OR
8.  NOR
9.  XOR
10. SHR
11. SHL

Please enter an operator option: 3

-------------------------------------------------------------------------------
10101 * 0x19ac =
HEX: 0x21b1c | BINARY: 100001101100011100 | FLOAT: 138012.0 | SEM: 01000011011000111000000000000000
-------------------------------------------------------------------------------

Enter (1) to see first input conversion values
Enter (2) to see second input conversion values
Enter (3) to see results conversions
Enter (0) to exit
0
Exiting AtomicRobotLemur Calculator!
```
AND
```
Do you wish to use the convertor or calculator?
Please enter 1 for the convertor, 2 for the calculator, or 0 to exit
2    

Welcome to the Calculator App!
Please enter a number: 10101

-------------------------------------------------------------------------------
Given: 10101

HEX: 0x15 | BINARY: 10101 | FLOAT: 21.0 | SEM: 01000001010000000000000000000000
-------------------------------------------------------------------------------

Please enter a number: 1101

-------------------------------------------------------------------------------
Given: 1101

HEX: 0xd | BINARY: 1101 | FLOAT: 13.0 | SEM: 01000001010000000000000000000000
-------------------------------------------------------------------------------

Allowable operations:
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  AND
6.  NOT
7.  OR
8.  NOR
9.  XOR
10. SHR
11. SHL

Please enter an operator option: 5

-------------------------------------------------------------------------------
10101 & 1101 =
HEX: 0x5 | BINARY: 101 | FLOAT: 5.0 | SEM: 01000000010000000000000000000000
-------------------------------------------------------------------------------

Enter (1) to see first input conversion values
Enter (2) to see second input conversion values
Enter (3) to see results conversions
Enter (0) to exit
```
OR
```
Do you wish to use the convertor or calculator?
Please enter 1 for the convertor, 2 for the calculator, or 0 to exit
2

Welcome to the Calculator App!
Please enter a number: 10101

-------------------------------------------------------------------------------
Given: 10101

HEX: 0x15 | BINARY: 10101 | FLOAT: 21.0 | SEM: 01000001010000000000000000000000
-------------------------------------------------------------------------------

Please enter a number: 11101

-------------------------------------------------------------------------------
Given: 11101

HEX: 0x1d | BINARY: 11101 | FLOAT: 29.0 | SEM: 01000011010000000000000000000000
-------------------------------------------------------------------------------

Allowable operations:
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  AND
6.  NOT
7.  OR
8.  NOR
9.  XOR
10. SHR
11. SHL

Please enter an operator option: 7

-------------------------------------------------------------------------------
10101 | 11101 =
HEX: 0x1d | BINARY: 11101 | FLOAT: 29.0 | SEM: 01000011010000000000000000000000
-------------------------------------------------------------------------------

Enter (1) to see first input conversion values
Enter (2) to see second input conversion values
Enter (3) to see results conversions
Enter (0) to exit
```
SHR/SHL
```
Do you wish to use the convertor or calculator?
Please enter 1 for the convertor, 2 for the calculator, or 0 to exit
2

Welcome to the Calculator App!
Please enter a number: 101011

-------------------------------------------------------------------------------
Given: 101011

HEX: 0x2b | BINARY: 101011 | FLOAT: 43.0 | SEM: 01000010110000000000000000000000
-------------------------------------------------------------------------------

Please enter a number: 4
Error - Failed to convert input!
Allowable operations:
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  AND
6.  NOT
7.  OR
8.  NOR
9.  XOR
10. SHR
11. SHL

Please enter an operator option: 11

-------------------------------------------------------------------------------
101011 << 4 =
HEX: 0x2b0 | BINARY: 1010110000 | FLOAT: 688.0 | SEM: 00101100000000000000000000000000
-------------------------------------------------------------------------------

Enter (1) to see first input conversion values
Enter (2) to see second input conversion values
Enter (3) to see results conversions
Enter (0) to exit
0
Exiting AtomicRobotLemur Calculator!
```
