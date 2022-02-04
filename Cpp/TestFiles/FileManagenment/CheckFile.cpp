#include <iostream>
#include <filesystem>

using std::cout; using std::cin;
namespace fs = std::filesystem;

const fs::path pathToShow{ argc >= 2 ? argv[1] : fs::current_path() };

for (const auto& entry : fs::directory_iterator(pathToShow)) {
    const auto filenameStr = entry.path().filename().string();
    if (entry.is_directory()) {
        cout << "dir:  " << filenameStr << '\n';
    }
    else if (entry.is_regular_file()) {
        cout << "file: " << filenameStr << '\n';
    }
    else
        cout << "??    " << filenameStr << '\n';
}
