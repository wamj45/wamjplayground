#include "bubblesort.h"
#include <iostream>
using namespace std;

int main()
{
  int array[] = {15, 2, 0, 33, 191, 1, 87, 49, 39, 11, 12, 49, 99};
  int n = sizeof(array) / sizeof(array[0]);
  sort(array, n);

  cout << "Sorted Array: \n";
  display_arr(array, n);

  cout << "Select a number to search for: " << endl;
  int search_val;
  cin >> search_val;

  bool ret = bin_search(array, n, search_val);

  cout << "Is value:[" << search_val <<"] in the array?" << endl;
  cout << boolalpha;
  cout << "Answer::[" << ret << "]" << endl;

  return 0;
}
