class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }

    public static ListNode deserialize(String data) {
        if (data == null || data.length() <= 2) {
            return null;
        }
        
        String[] nodes = data.substring(1, data.length() - 1).split(",");
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        for (String node : nodes) {
            current.next = new ListNode(Integer.parseInt(node.trim()));
            current = current.next;
        }
        
        return dummy.next;
    }

    public static String serialize(ListNode head) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        while (head != null) {
            sb.append(head.val);
            head = head.next;
            if (head != null) {
                sb.append(",");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        
        while (current != null && current.next != null) {
            if (current.val == current.next.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }
        
        return head;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        ListNode head = ListNode.deserialize("[1,1,2]");
        ListNode result = sol.deleteDuplicates(head);
        System.out.println(ListNode.serialize(result));  // Expected output: [1,2]
    }
}
