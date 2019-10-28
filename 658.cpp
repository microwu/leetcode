#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
	vector<int> findClosestElements(vector<int> &arr, int k, int x) {
		auto lit = arr.begin();
		auto rit = arr.begin()+k;
		vector<int> answer(lit,rit);
		while(rit!=arr.end()){
			if(abs(*rit-x)<abs(answer[0]-x)||abs(*rit-x)<abs(answer[k-1]-x)){
				answer.erase(answer.begin());
				answer.push_back(*rit);
			}
			rit++;
		}
		return answer;
	}
};

int main() {
	Solution s;
	vector<int> arr;
	vector<int> answer;
	arr.push_back(1);
	arr.push_back(2);
	arr.push_back(3);
	arr.push_back(4);
	arr.push_back(5);
	int k,x;
	k=4;
	x=3;
	answer = s.findClosestElements(arr,k,x);
	for(auto ele:answer){
		cout << ele << " ";
	}
	cout << endl;
	return 0;
}
