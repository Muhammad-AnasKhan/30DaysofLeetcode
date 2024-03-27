/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// recursively examining their left and right subtrees,

class Solution {

    public boolean isSameTree(TreeNode p, TreeNode q) {
        return depth_first_search(p , q);       
    }

    public boolean depth_first_search(TreeNode node_1 , TreeNode node_2){

        if((node_1 == null) && (node_2 == null)){
            return true;
        }

        if(((node_1 == null) && (node_2 != null)) || ((node_1 != null) && (node_2 == null))){
            return false;
        }

        if(node_1.val != node_2.val){
            return false;
        }

        boolean left_subtree_match = depth_first_search(node_1.left , node_2.left);

        boolean right_subtree_match = depth_first_search(node_1.right , node_2.right);

        return (left_subtree_match && right_subtree_match);
    }
}