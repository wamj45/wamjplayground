#include <iostream>
#include <vector>
#include <dirent.h>
#include <string>

using namespace std;

int main() {
  DIR *dir;
  struct dirent *diread;
  vector<char *> files;
  // string dir_path = "/Users/wamj45/Downloads";

if ((dir = opendir("/Users/wamj45/Downloads/")) != nullptr) {
  while ((diread = readdir(dir)) != nullptr) {
    files.push_back(diread->d_name);
  }
  closedir(dir);
}
else {
  perror ("opendir");
  return EXIT_FAILURE;
}

  for (auto file : files) cout << file << endl;
  cout << endl;

  return EXIT_SUCCESS;
}
