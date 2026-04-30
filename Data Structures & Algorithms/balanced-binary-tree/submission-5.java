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

class Solution {
    int diff=0;
    public int dfs(TreeNode root){
        if (root==null){
            return 0;
        }
        int left=dfs(root.left);
        int right=dfs(root.right);
        diff=Math.max(diff,Math.abs(right-left));
        return Math.max(1+dfs(root.left),1+dfs(root.right));

    }


    public boolean isBalanced(TreeNode root) {
        dfs(root);
        if (diff>1){
            return false;
        }
        else{
            return true;
        }
    }
}
