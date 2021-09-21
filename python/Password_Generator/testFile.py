import os
import sys
import json


class ReadFile():

    def __init__(self,file):
        self.file = file

    def readFile(self):
        with open(self.file) as f:
            data = f.read()

        jsonData = json.loads(data)

        counter = 0
        for line in data:
            print('here')
            print(jsonData['google.com'])
            counter+=1
        f.close()
        return True

def main():
    file = "PasswordManager.txt"

    read = ReadFile(file)
    if read.readFile() is False:
        print("Error - Unable to open file")
        sys.exit(0)

    print('Done!')

if __name__ == '__main__':
    main()
