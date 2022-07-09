/*
 * This is code I wrote while watching "Linked Lists for Technical Interviews - Full Course"
 * by Alvin the Programmer. Here's a link to the video :
 * https://www.youtube.com/watch?v=Hj_rA0dhr2I
 * He codes in Javascript, but I've transcribed it into Java.
 */

class LinkedList {

    Node head;

    static class Node {
        int val;
        Node next;
        Node(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public static void traverse(Node head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.print("\n");
    }

    public static void traverseRecursive(Node head) {
        if (head == null) {
            System.out.print("\n");
            return;
        }
        System.out.print(head.val + " ");
        traverseRecursive(head.next);
    }

    public static int sumList(Node head) {
        int sum = 0;
        while (head != null) {
            sum += head.val;
            head = head.next;
        }
        return sum;
    }

    public static int sumListRecursive(Node head) {
        if (head == null) {
            return 0;
        }
        return head.val + sumListRecursive(head.next);
    }

    public static boolean find(Node head, int target) {
        while(head != null) {
            if(head.val == target) {
                return true;
            }
            head = head.next;
        }
        return false;
    }

    public static boolean findRecursive(Node head, int target) {
        if (head == null) {
            return false;
        }
        if (head.val == target) {
            return true;
        }
        return findRecursive(head.next, target);
    }

    public static int getNodeAtIndex(Node head, int idx) {
        int p = 0;
        while (head != null) {
            if(p == idx)
            {
                return head.val;
            }
            p++;
            head = head.next;
        }
        return -1;
    }

    public static int getNodeAtIndexRecusive(Node head, int idx) {
        if (head == null) {
            return -1;
        }
        if (idx == 0) {
            return head.val;
        }
        return getNodeAtIndexRecusive(head.next, idx-1);
    }

    public static Node reverse(Node head) {
        Node prev = null;
        Node curr = head;

        while (curr != null) {
            Node next = curr.next;
            // Null a -> b -> c
            // prev cur next
            curr.next = prev;
            // Null <- a   b -> c
            // prev cur   next
            prev = curr;
            curr = next;
            // Null <- a    b -> c
            //        prev cur  next
        }
        head = prev;
        return head;
    }

    public static Node reverseRecursive(Node head) {
        // if the head is null or the list
        // contains only one element then reversing the list
        // does not have any impact on the list. Therefore, we
        // can return the original list without performing any operation
        if (head == null || head.next == null) {
            return head;
        }

        // reverse the rest (r) of the list and place
        // the first element of the list at the last
        Node r = reverseRecursive(head.next);
        head.next.next = head;
        head.next = null;
        // fixing the head pointer
        return r;
    }

    public static Node ziiperLists(Node head1, Node head2) {
        Node tail = head1;
        Node current1 = head1.next; //we start with the first list.
        Node current2 = head2;
        int count = 0;

        while (current1 != null && current2 != null) {
            if (count % 2 == 0) {
                tail.next = current2;
                current2 = current2.next;
            } else {
                tail.next = current1;
                current1 = current1.next;
            }
            tail = tail.next;
            count += 1;
        }

        if (current1 != null) {
            tail.next = current1;
        }
        if (current2 != null) {
            tail.next = current2;
        }
        return head1;
    }

    public static Node ziiperListsRecursive(Node head1, Node head2) {
        if (head1 == null && head2 == null) {
            return null;
        }
        if (head1 == null) {
            return head2;
        }
        if (head2 == null) {
            return head1;
        }
        Node next1 = head1.next;
        Node next2 = head2.next;
        head1.next = head2;
        head2.next = ziiperListsRecursive(next1, next2);
        return head1;
    }



    public static void main(String[] args) {

        LinkedList llist = new LinkedList();

        llist.head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);

        /* SO far, the LL looks like this:
         * +----+------+ +----+------+ +----+------+
         * | 1 | null | | 2 | null | | 3 | null |
         * +----+------+ +----+------+ +----+------+
         */
        llist.head.next = second;
        second.next = third;
        /*
         * Now the LL looks like this:
         * +----+------+ +----+------+ +----+------+
         * | 1 | o-------->| 2 | o-------->| 3 | null |
         * +----+------+ +----+------+ +----+------+
         */
        // OPERATIONS : -

        traverse(llist.head);
        traverseRecursive(llist.head);

        System.out.println(sumList(llist.head));
        System.out.println(sumListRecursive(llist.head));

        System.out.println(find(llist.head, 9));
        System.out.println(find(llist.head, 2));
        System.out.println(findRecursive(llist.head, 9));
        System.out.println(findRecursive(llist.head, 2));

        System.out.println(getNodeAtIndex(llist.head, 0));
        System.out.println(getNodeAtIndex(llist.head, 1));
        System.out.println(getNodeAtIndex(llist.head, 2));
        System.out.println(getNodeAtIndex(llist.head, 3));
        System.out.println(getNodeAtIndexRecusive(llist.head, 0));
        System.out.println(getNodeAtIndexRecusive(llist.head, 1));
        System.out.println(getNodeAtIndexRecusive(llist.head, 2));
        System.out.println(getNodeAtIndexRecusive(llist.head, 3));

        llist.head = reverse(llist.head);
        traverse(llist.head);
        llist.head = reverseRecursive(llist.head);
        traverse(llist.head);

        // Creating two LLs to zip together.
        LinkedList llist1 = new LinkedList();
        llist1.head = new Node(11);
        Node second1 = new Node(22);
        Node third1 = new Node(33);
        llist1.head.next = second1;
        second1.next = third1;
        LinkedList llist2 = new LinkedList();
        llist2.head = new Node(44);
        Node second2 = new Node(55);
        Node third2 = new Node(66);
        llist2.head.next = second2;
        second2.next = third2;
        traverse(ziiperLists(llist1.head, llist2.head));
        // Creating two more LLs to zip together.
        LinkedList llist3 = new LinkedList();
        llist3.head = new Node(11);
        Node second3 = new Node(22);
        Node third3 = new Node(33);
        llist3.head.next = second3;
        second3.next = third3;
        LinkedList llist4 = new LinkedList();
        llist4.head = new Node(44);
        Node second4 = new Node(55);
        Node third4 = new Node(66);
        llist4.head.next = second4;
        second4.next = third4;
        traverse(ziiperListsRecursive(llist3.head, llist4.head));

    }
}
