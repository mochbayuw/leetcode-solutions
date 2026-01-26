class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevGroup = dummy;

        while (true) {
            // cek ada k node atau tidak
            ListNode kth = prevGroup;
            for (int i = 0; i < k && kth != null; i++) {
                kth = kth.next;
            }
            if (kth == null) break;

            ListNode groupNext = kth.next;

            // reverse group
            ListNode prev = groupNext;
            ListNode curr = prevGroup.next;

            while (curr != groupNext) {
                ListNode tmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = tmp;
            }

            // connect
            ListNode tmp = prevGroup.next;
            prevGroup.next = kth;
            prevGroup = tmp;
        }

        return dummy.next;
    }
}
