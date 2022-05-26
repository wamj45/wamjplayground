#include <iostream>
#include "math_op.h"

using namespace std;

int main() {
  int a, b;
  float x, y, z;

  cout << "Please enter a number: " << endl;
  cin >> a;

  cout << "Enter another number: " << endl;
  cin >> b;

  x = 15.2;
  y = 3.12;
  z = division(x, y);

  int ans = addition(a, b);
  float add_float = addition(x, y);

  cout << "Additon result: " << ans << endl;
  cout << "Division result: " << z << endl;
  cout << "Float Add: " << add_float << endl;

  return 0;
}
