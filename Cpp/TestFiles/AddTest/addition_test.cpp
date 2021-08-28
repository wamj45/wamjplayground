#include <iostream>
int main()
{
  std::cout << "Enter two numbers:" << std::endl;
  double v1 = 0, v2 = 0; //Made into a double to handle addition of doubles
  std::cin >> v1 >> v2;
  std::cout << "The sum of " << v1 << " and " << v2
            << " is " << v1+v2 << std::endl;
  /* code */
  return 0;
}
