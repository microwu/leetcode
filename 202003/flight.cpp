#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
  private:
    vector<int> flightInfo;
    vector<vector<int> > allBook;

  public:
    void book(vector<int> info) {
        int i = info[0]-1, j = info[1]-1, k = info[2];
        // cout << "i:" << i << " j:" << j << " k:" << k << endl;
        for (int current = i; current <= j; current++) {
            flightInfo[current] += k;
        }
    }
    Solution(int size, vector<vector<int> > allBook) {
        for (int i = 0; i < size; i++) {
            flightInfo.push_back(0);
        }
        this->allBook = allBook;
        for (auto info : allBook) {
            book(info);
        }
    }
    void display() {
        for (int i = 0; i < flightInfo.size(); i++) {
            if (i != int(flightInfo.size() - 1)) {
                cout << flightInfo[i] << ",";
            } else {
                cout << flightInfo[i] << endl;
            }
        }
    }
};

bool isFinalLine(string input) {
    // cout << input.length() << endl;
    for (auto c : input) {
        if (c == ',') {
            return false;
        }
    }
    // cout << "isFinal" << endl;
    return true;
}

int string2int(string s) {
    int number = 0;
    for (auto c : s) {
        // cout << c << endl;
        number = number * 10 + int(c - '0');
    }
    return number;
}

vector<int> split(string s) {
    vector<int> info;
    string num = "";
    for (auto c : s) {
        if (c >= '0' && c <= '9') {
            num.push_back(c);
        } else if (c == ',') {
            info.push_back(string2int(num));
            num = "";
        }
    }
    info.push_back(string2int(num));
    return info;
}

int main(int argc, char const* argv[]) {
    vector<vector<int> > allBook;
    string inputLine;
    while(true) {
        cin >> inputLine;
        if(isFinalLine(inputLine)){
            break;
        }
        vector<int> info = split(inputLine);
        allBook.push_back(info);
    }
    int flightSize = string2int(inputLine);
    Solution solution(flightSize, allBook);
    solution.display();
    // cout << flightSize << endl;
    return 0;
}
