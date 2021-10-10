#include <iostream>
using namespace std;

int main()
{
  double v1 = 0, v2 = 0; //Made into a double to handle addition of doubles
  double sum;
  cout << "Enter two numbers:" << std::endl;
  cin >> v1 >> v2;
  sum = v1 + v2;
  cout << "The sum of " << v1 << " and " << v2
            << " is " << sum << std::endl;
  /* code */
  return 0;
}
