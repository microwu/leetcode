#include <iostream>
#include <list>
#include <vector>

using namespace std;

class Solution {
    vector<vector<int> > pair_list;

   public:
    Solution(list<vector<int> > pair_list);
    int longest_length() {
        int length = 1;
        vector<int> current_tail = pair_list[0];
        for (int i = 1; i < int(pair_list.size()); i++) {
            // if pair_list[i] can be added to the list
            if (current_tail[1] < pair_list[i][0]) {
                length++;
                current_tail = pair_list[i];
            }
        }
        return length;
    }
};

int Compare(vector<int> left, vector<int> right) { return left[1] < right[1]; }

Solution::Solution(list<vector<int> > pair_list) {
    pair_list.sort(Compare);
    for (auto pair : pair_list) {
        this->pair_list.push_back(pair);
        cout << pair[0] << ',' << pair[1] << endl;
    }
        cout << "-----"<<endl;
    for (auto pair: this->pair_list){
        cout << pair[0] << ',' << pair[1] << endl;
    }
}

int main() {
    list<vector<int> > pair_list;
    int len;
    cin >> len;
    for (int i = 0; i < len; i++) {
        int left, right;
        vector<int> pair;
        cin >> left;
        cin >> right;
        pair.push_back(left);
        pair.push_back(right);
        pair_list.push_back(pair);
    }
    Solution s(pair_list);
    cout << s.longest_length() << endl;
    return 0;
}
