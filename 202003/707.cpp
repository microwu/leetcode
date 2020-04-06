#include <iostream>
using namespace std;

struct Node {
	int val;
	Node *next;
	Node *prev;
	Node() {
		next = NULL;
		prev = NULL;
	}
	Node(int val, Node *next, Node *prev) {
		this->val = val;
		this->next = next;
		this->prev = prev;
	}
};

class MyLinkedList {
  private:
	Node *root;

  public:
	/** Initialize your data structure here. */
	MyLinkedList() { root = NULL; }

	/** Get the value of the index-th node in the linked list. If the index is
	 * invalid, return -1. */
	int get(int index) {
		Node *now = root;
		int i = 0;
		while (now != NULL) {
			if (i == index) {
				return now->val;
			}
			now = now->next;
			i++;
		}
		return -1;
	}

	/** Add a node of value val before the first element of the linked list.
	 * After the insertion, the new node will be the first node of the linked
	 * list. */
	void addAtHead(int val) {
		if (root == NULL) {
			root = new Node(val, NULL, NULL);
		} else {
			root->prev = new Node(val, root, NULL);
			root = root->prev;
		}
	}

	/** Append a node of value val to the last element of the linked list. */
	void addAtTail(int val) {
		Node *tail = root;
		if (tail == NULL) {
			tail = new Node(val, NULL, NULL);
		} else {
			while (tail->next != NULL) {
				tail = tail->next;
			}
			tail->next = new Node(val, NULL, tail);
		}
	}

	/** Add a node of value val before the index-th node in the linked list. If
	 * index equals to the length of linked list, the node will be appended to
	 * the end of linked list. If index is greater than the length, the node
	 * will not be inserted. */
	void addAtIndex(int index, int val) {
		if (index <= 0) {
			addAtHead(val);
			return;
		}
		Node *now = root;
		int length = 0;
		bool flag = false;
		while (now != NULL) {
			if (length == index) {
				Node *temp = now->prev;
				now->prev = new Node(val, now, temp);
				temp->next = now->prev;
				flag=true;
				break;
			}
			now = now->next;
			length++;
		}
		if (length == index && flag==false) {
			addAtTail(val);
		}
	}

	/** Delete the index-th node in the linked list, if the index is valid. */
	void deleteAtIndex(int index) {
		Node *now = root;
		int length = 0;
		while (now != NULL) {
			if (length == index) {
				if (now->next != NULL) { // not tail node
					now->next->prev = now->prev;
				}
				if (now->prev != NULL) { // not head node
					now->prev->next = now->next;
				}
				if (now->prev == NULL) {
					root = now->next;
				}
				delete now;
				break;
			}
			now = now->next;
			length++;
		}
	}

	void display() {
		Node *now = root;
		while (now != NULL) {
			cout << now->val << " ";
			now = now->next;
		}
		cout << endl;
	}
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */

int main(int argc, char const *argv[]) {
	MyLinkedList linkedList;
	linkedList.addAtHead(7);	 // 7
	linkedList.addAtHead(2);	 // 2 7
	linkedList.addAtTail(1);	 // 2 7 1
	linkedList.addAtIndex(3, 0); // 2 7 1 0
	linkedList.display();
	linkedList.deleteAtIndex(2); // 2 7 0
	linkedList.addAtHead(6);	 // 6 2 7 0
	linkedList.addAtTail(4);	 // 6 2 7 0 4
	linkedList.display();
	cout << linkedList.get(4) << endl;
	linkedList.addAtHead(4);	// 4 6 2 7 0 4
	linkedList.display();
	linkedList.addAtIndex(5, 0);	// 4 6 2 7 0 0 4
	cout << __LINE__ << ":";
	linkedList.display();
	linkedList.addAtHead(6);	// 6 4 6 2 7 0 4 0
	linkedList.display();

	return 0;
}
