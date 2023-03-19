#include <cmath>
#include <cstring>
#include <queue>
#include <vector>

#include "leetcode/leetcode.h"
using namespace std;

template <class T>
ostream& operator<<(ostream& stream, const vector<T>& nums) {
    stream << "[ ";
    for (auto beg = nums.cbegin(); beg != nums.cend(); ++beg) {
        stream << *beg << " ";
    }
    return stream << "]";
}

template <class T>
istream& operator>>(istream& stream, vector<T>& nums) {
    char cstr[65536];
    stream.getline(cstr, 65535);
    if (strlen(cstr) == 0) {
        stream.getline(cstr, 65535);
    }
    string str = string(cstr);
    vector<string> real_nums;
    real_nums = split(str, " ");
    cout << str << "[" << real_nums.size() << "] ";
    for (auto beg = real_nums.cbegin(); beg != real_nums.cend(); ++beg) {
        nums.push_back(atoi((*beg).c_str()));
        cout << nums.back() << " ";
    }
    cout << endl;
    return stream;
}

// ________________________________________________________

class Solution {
public:
};

// ________________________________________________________

int main() {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cout << "nums: " << nums << endl;
    // close io sync
    ios::sync_with_stdio(false);
    // cin.tie(NULL);
}
