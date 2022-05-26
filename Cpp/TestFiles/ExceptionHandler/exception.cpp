#include <iostream>
#include <string>

using namespace std;

float divide_func(float x, float y)
{
  if (y == 0) {
    throw "Divide by Zero Error!!!";
  }
  return (x / y);
}

float get_value()
{
  float input;
  string prompt = "Please enter a number: \n";

  cout << prompt;
  cin >> input;
  return input;
  }

int main()
{
  float x, y, z;

  try {
  x = get_value();
  y = get_value();
  }
  catch(...) {
    cerr << "Error!" << endl;
  }

  try {
    z = divide_func(x, y);
    cout << "\nGiven " << x << " / " << y << " = " << z << endl;
  }
  catch(const char* e_msg) {
    cerr << e_msg << endl;
  }

  return 0;
}
