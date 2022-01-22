#include <iostream>
#include <string>
#include <filesystem>
#include <unistd.h>

using std::cout; using std::cin;
using std::endl; using std::string;
using std::filesystem::current_path;

int main() {

    cout << "Current working directory: " << current_path() << endl;

    return EXIT_SUCCESS;
}
