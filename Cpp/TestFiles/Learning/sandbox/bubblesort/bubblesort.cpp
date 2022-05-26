#include "bubblesort.h"
#include <iostream>

using namespace std;

void sort(int arr[], int n)
{
  int i, j;
  // This outer loop runs for the number of elements in the array minus 1
  for (i = 0; i < n - 1; i++)
  {
    // Inner loop handles the swap
    for (j =0; j < n-1; j++)
    {
      if (arr[j] > arr[j+1]) {swap(arr[j], arr[j+1]);}
    }
  }
}

void display_arr(int arr[], int size)
{
  int i;
  for (i = 0; i < size; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
}

bool bin_search(int arr[], int size, int target)
{
  // check the middle until we find the proper value
  int first = 0;
  int mid;

  while (first < size)
  {
    mid = ((size - 1) + first) / 2;
    if (arr[mid] == target) {return true;}
    else if (arr[mid] < target) {first = mid + 1;}
    else {size = mid - 1;}
  }
  return false;
}
