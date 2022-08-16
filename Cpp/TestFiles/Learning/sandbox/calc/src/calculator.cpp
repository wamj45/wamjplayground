#include <iostream>
#include "math_op.h"


int main() {
  int a, b;
  float x, y, z;

  std::cout << "Please enter a number: " << endl;
  std::cin >> a;

  std::cout << "Enter another number: " << endl;
  std::cin >> b;

  x = 15.2;
  y = 3.12;
  z = division(x, y);

  int ans = addition(a, b);
  float add_float = addition(x, y);

  std::cout << "Additon result: " << ans << endl;
  std::cout << "Division result: " << z << endl;
  std::cout << "Float Add: " << add_float << endl;

  return 0;
}
