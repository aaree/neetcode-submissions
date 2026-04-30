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
    public TreeNode invertTree(TreeNode root) {
        if (root==null){
            return null;
        }
        Deque<TreeNode> deque=new ArrayDeque<>();
        deque.offer(root);
        TreeNode temp;
        while(!deque.isEmpty()){
            TreeNode curr=deque.poll();
            temp=curr.left;
            curr.left=curr.right;
            curr.right=temp;
            if (curr.right!=null){
                deque.add(curr.right);
            }
            if (curr.left!=null){
                deque.add(curr.left);
            }


        }
        return root;

    }

}
