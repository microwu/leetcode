#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
    int k;
    string s;

  public:
    Solution(string s, int k);
    int longest_substr_len() {
        int length = 0;
        int left = 0;
        int max_repeat = 0;
        vector<int> count(26,0);
        for (int right = 0; right < int(s.length()); right++) {
            // initial window
            count[s[right] - 'A']++;
            max_repeat = max_repeat > count[s[right] - 'A']
                            ? max_repeat
                            : count[s[right] - 'A'];

            // if the window is overflow
            if (right - left + 1 > max_repeat + k) {
                count[s[left] - 'A']--;
                left++;
            }
            length = length > right - left + 1 ? length : right - left + 1;
        }
        return length;
    }
};

Solution::Solution(string s, int k) {
    this->s = s;
    this->k = k;
}

int main(int argc, char const* argv[]) {
    if (argc == 3) {
        string s(argv[1]);
        int k;
        k = atoi(argv[2]);
        Solution soution(s, k);
        cout << soution.longest_substr_len() << endl;
    }
    return 0;
}
