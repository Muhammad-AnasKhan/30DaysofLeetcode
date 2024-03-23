/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

private:
    vector<vector<int>> res;
    void newLevel(TreeNode* node, int level)
    {
        if(node == nullptr) return;
        if(res.size() == level) res.push_back({});
        res[level].push_back(node->val);
        newLevel(node->left, level+1);
        newLevel(node->right, level+1);
    }

public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        newLevel(root, 0);
        return res;
    }
};