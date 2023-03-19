#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(const string& str, const string& delim) {
    string::size_type slow = 0, fast = str.find(delim);
    vector<string> res;
    while (fast != string::npos) {
        res.push_back(str.substr(slow, fast - slow));
        slow = fast + delim.size();
        fast = str.find(delim, slow);
    }
    if (slow != str.size()) res.push_back(str.substr(slow));
    return res;
}

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};
