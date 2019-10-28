#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

void display(ListNode *root);

class Solution {
  public:
	vector<ListNode *> splitListToParts(ListNode *root, int k) {
		vector<ListNode *> answer;
		ListNode *temp = root;
		int size = 0;
		// get list size
		while (temp != NULL) {
			size++;
			temp = temp->next;
		}
		if (size != 0) {
			// init temp pointer
			temp = root;
			int long_count = size % k; // how many long list (length = size/k+1)
			int length = 0;			   // length for each kid list
			ListNode *ele_root = new ListNode(
				root->val);	  // root node for each elements in answer
			ListNode *node_p; //= ele_root; // temp pointer for element nodes

			while (temp != NULL) {
				// add elements to result before the kid list readed
				if (length == 0) {
					ele_root = new ListNode(temp->val);
					node_p = ele_root;
					answer.push_back(ele_root);
					long_count--;
				} else if (long_count >= 0 && length < (size / k) + 1) {
					node_p->next = new ListNode(temp->val);
					node_p = node_p->next;
				} else if (long_count < 0 && length < size / k) {
					node_p->next = new ListNode(temp->val);
					node_p = node_p->next;
				} else {
					length = 0;
					continue;
				}
				temp = temp->next;
				length++;
			}
		}

		while ((int)answer.size() < k) {
			answer.push_back(NULL);
		}
		return answer;
	}
};

void display(ListNode *root) {
	while (root != NULL) {
		cout << root->val << " ";
		root = root->next;
	}
	cout << endl;
}

int main() {
	ListNode *root, *temp;
	root = new ListNode(1);
	root->next = new ListNode(2);
	temp = root->next;
	temp->next = new ListNode(3);
	temp = temp->next;
	temp->next = new ListNode(4);
	temp = temp->next;
	temp->next = new ListNode(5);
	temp = temp->next;
	temp->next = new ListNode(6);
	temp = temp->next;
	temp->next = new ListNode(7);
	temp = temp->next;
	Solution s;
	vector<ListNode *> answer = s.splitListToParts(root, 3);
	display(root);
	for (int i = 0; i < (int)answer.size(); i++) {
		if (answer[i] != NULL) {
			display(answer[i]);
		}
	}
	return 0;
}
