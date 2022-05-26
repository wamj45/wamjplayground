import os, time
from calculator import Calculator
from single_input_handler import InputHandler

def main():
    input_handler1 = InputHandler()
    calc = Calculator()

    # while True:
    try:
        choice = int(input("Do you wish to use the convertor or calculator?\nPlease enter 1 for the convertor, 2 for the calulator, or 0 to exit\n"))
        if choice == 1:
            if input_handler1.run() is False:
                print("Error - Failed to run Converter")
                os._exit(255)
        elif choice == 2:
            if calc.run() is False:
                print("Error - Failed to run Calculator")
                os._exit(2)
        elif choice == 0:
            print("Exiting App...")
            os._exit(0)
        else:
            print("Invaild Operation selected!\nPlease restart app and enter valid calculator function.")
            os._exit(254)
        time.sleep(1)

    except KeyboardInterrupt as kb:
        print("\nUser Exit Intiated")
        os._exit(0)

if __name__ == '__main__':
    main()
