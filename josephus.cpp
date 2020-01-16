#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

class Josephus {
   private:
    int* loop;
    int size;
    int count;

   public:
    Josephus(int size, int count) {
        this->size = size;
        this->count = count;
        loop = new int[size];
        for (int i = 0; i < size; i++) {
            loop[i] = i + 1;
        }
        count = 3;
    }
    int solution() {
        int index = 0;
        int out = 0;
        int count = 0;
        while (out < size - 1) {
            index %= size;
            if (loop[index] != 0) {
                count++;
                if (count == this->count) {
                    loop[index] = 0;
                    out++;
                    count = 0;
                    // display();
                }
            }
            index++;
        }
        return (index + this->count) % size + 1;
    }
    void display() {
        for (int i = 0; i < size; i++) {
            cout << loop[i] << " ";
        }
        cout << endl;
    }
};

int main(int argc, char const* argv[]) {
    int size, count;
    // cin >> size;
    stringstream geek(argv[1]);
    stringstream countgeek(argv[2]);
    geek >> size;
    countgeek >> count;
    cout << "size:" << size << endl;
    Josephus josephus_loop(size, count);
    cout << "Solution:" << josephus_loop.solution() << endl;
    cout << "loop:";
    josephus_loop.display();
    return 0;
}
