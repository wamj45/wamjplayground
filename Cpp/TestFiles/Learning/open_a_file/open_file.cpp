#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

  fstream newfile;
  newfile.open("testing.txt", ios::out);

  // Overwrites whatever is in the first line with new text
  // Need to find next empty line
  if (newfile.is_open())
  {
    newfile << "testing \n";
    newfile.close();
  }

  newfile.open("testing.txt", ios::in);
  if (newfile.is_open())
  {
    string temp;
    while (getline(newfile, temp))
    {
      cout << temp << "\n";
    }
    newfile.close();
  }
  return 0;
}
