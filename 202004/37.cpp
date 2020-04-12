#include <iostream>
#include <set>
#include <stack>
#include <vector>
using namespace std;

class Solution {
   public:
    set<int> check(vector<vector<char> > board, int num_i, int num_j) {
        set<int> valid;
        for (int i = 1; i <= 9; i++) {
            valid.insert(i);
        }
        for (int i = 0; i < 9; i++) {
            if (board[i][num_j] != '.') {
                valid.erase(board[i][num_j] - '0');
            }
            if (board[num_i][i] != '.') {
                valid.erase(board[num_i][i] - '0');
            }
        }
        for (int i = (num_i / 3) * 3; i < (num_i / 3) * 3 + 3; i++) {
            for (int j = (num_j / 3) * 3; j < (num_j / 3) * 3 + 3; j++) {
                if (board[i][j] != '.') {
                    valid.erase(board[i][j] - '0');
                }
            }
        }
        return valid;
    }
    bool solveSudoku(vector<vector<char> >& board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    int k = 1;
                    bool flag = false;
                    for (int num : check(board, i, j)) {
                        board[i][j] = '0' + num;
                        if (solveSudoku(board)) {
                            flag = true;
                            break;
                        } else {
                            board[i][j] = '.';
                        }
                    }
                    if (!flag) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
void print(vector<vector<char> > board) {
    for (auto row : board) {
        for (auto num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
}

int main() {
    // char temp[9][9] = {{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
    //                    {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
    //                    {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
    //                    {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
    //                    {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
    //                    {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
    //                    {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
    //                    {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
    //                    {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
    char temp[9][9] = {{'8', '.', '.', '.', '.', '.', '.', '.', '.'},
                       {'.', '.', '3', '6', '.', '.', '.', '.', '.'},
                       {'.', '7', '.', '.', '9', '.', '2', '.', '.'},
                       {'.', '5', '.', '.', '.', '7', '.', '.', '.'},
                       {'.', '.', '.', '.', '4', '5', '7', '.', '.'},
                       {'.', '.', '.', '1', '.', '.', '.', '3', '.'},
                       {'.', '.', '1', '.', '.', '.', '.', '6', '8'},
                       {'.', '.', '8', '5', '.', '.', '.', '1', '.'},
                       {'.', '9', '.', '.', '.', '.', '4', '.', '.'}};
    vector<vector<char> > board;
    for (int i = 0; i < 9; i++) {
        vector<char> row;
        for (int j = 0; j < 9; j++) {
            row.push_back(temp[i][j]);
        }
        board.push_back(row);
    }
    print(board);
    cout << endl;
    Solution s;
    s.solveSudoku(board);
    print(board);
    return 0;
}
