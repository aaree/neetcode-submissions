/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        if (head==null||head.next == null){
            return;
        }
        ListNode prev=null;
        ListNode fast=head;
        ListNode slow=head;
        ListNode ans=new ListNode(0);
        ListNode dummy=head;
        while ((fast!=null)&&(fast.next!=null)){
            prev=slow;
            slow=slow.next;
            fast=fast.next.next;
        }
        prev.next=null;
        ListNode temp=null;
        ListNode prev2=null;
        while (slow!=null){
            temp=slow.next;
            slow.next=prev2;
            prev2=slow;
            slow=temp;
        }
        while ((dummy!=null)&&(prev2!=null)){
            ListNode t1=dummy.next;
            ListNode t2=prev2.next;
            dummy.next=prev2;
            if (t1==null){
                break;
            }
            prev2.next=t1;
            //t1.next=t2;
            dummy=t1;
            prev2=t2;
        }
        
    }
}
