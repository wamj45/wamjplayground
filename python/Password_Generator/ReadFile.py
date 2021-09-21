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
            numLines = self.getNumLines(f)
            print(f"This is the number of lines in the file: [{numLines}]")

            counter = 0
            while counter < numLines:
                print(counter)
                for line in data:
                    print('here')
                    print(jsonData['google.com'])
                    counter+=1
                    print('Back to top')
                    break
        f.close()
        return True

    def getNumLines(self, file):
        x = 0
        for x, l in enumerate(file):
            pass
        return x + 1


def main():
    file = "PasswordManager.txt"

    read = ReadFile(file)
    if read.readFile() is False:
        print("Error - Unable to open file")
        sys.exit(0)

    print('Done!')

if __name__ == '__main__':
    main()
