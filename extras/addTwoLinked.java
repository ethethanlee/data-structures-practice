package extras;

public class addTwoLinked {
    static ListNode l;

    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; 
        }
    }
 
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        boolean ones = false;
        ListNode finger = l1;
        ListNode otherFinger = l2;
        if ((l1.val + l2.val) > 9) {
            l1.val = l1.val + l2.val - 10;
            ones = true;
        }
        else {
            l1.val = l1.val + l2.val;
        }
        
        
        while (!(finger.next == null) || !(otherFinger.next == null)) {
            if (finger.next == null) {
                ListNode temp = new ListNode(0);
                finger.next = temp;
            }
            if (otherFinger.next == null) {
                ListNode temp = new ListNode(0);
                otherFinger.next = temp;
            }
            
            if (ones) {
                if ((finger.next.val + otherFinger.next.val + 1) > 9) {
                    finger.next.val = 
                        finger.next.val + otherFinger.next.val - 10 + 1;
                    finger = finger.next;
                    otherFinger = otherFinger.next;
                }
                else {
                    finger.next.val = finger.next.val + otherFinger.next.val + 1;
                    finger = finger.next;
                    otherFinger = otherFinger.next;
                    ones = false;
                }
                
            }
            else {
                if ((finger.next.val + otherFinger.next.val) > 9) {
                    finger.next.val = 
                        finger.next.val + otherFinger.next.val - 10;
                    finger = finger.next;
                    otherFinger = otherFinger.next;
                    ones = true;
                }
                else {
                    finger.next.val = finger.next.val + otherFinger.next.val;
                    finger = finger.next;
                    otherFinger = otherFinger.next;
                }
            }
        }
        if (ones){
            ListNode temp = new ListNode(1);
            finger.next = temp;
        }
        return l1;

        
    }

    public static void main(String[] args) {
        System.out.println("asdf");
        ListNode l1 = new ListNode();
        ListNode l2 = new ListNode();
        ListNode l3 = new ListNode();
        System.out.println("asdf");
        l1.val = 3;
        l2.val = 4;
        l3.val = 3;
        l1.next = l2;
        l2.next = l3;
        l3.next = null;
        System.out.println("asdf");
        System.out.println(addTwoNumbers(l1, l1).toString());

        
    }
}
