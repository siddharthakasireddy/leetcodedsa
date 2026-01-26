class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s;
        preorder(root, s);
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<int> vals;
        stringstream ss(data);
        int x;
        while (ss >> x) vals.push_back(x);

        int idx = 0;
        return build(vals, idx, INT_MIN, INT_MAX);
    }

private:
    void preorder(TreeNode* root, string& s) {
        if (!root) return;
        s += to_string(root->val) + " ";
        preorder(root->left, s);
        preorder(root->right, s);
    }

    TreeNode* build(vector<int>& vals, int& idx, int low, int high) {
        if (idx >= vals.size()) return nullptr;
        int val = vals[idx];
        if (val < low || val > high) return nullptr;

        idx++;
        TreeNode* node = new TreeNode(val);
        node->left = build(vals, idx, low, val);
        node->right = build(vals, idx, val, high);
        return node;
    }
};
