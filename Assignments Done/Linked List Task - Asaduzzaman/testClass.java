package com.codeKat;

// Task 3 :	Write a Test class to test your code.
public class testClass {

    public static void main(String[] args) {
        // Creating a SList instance named 'll'.
        SList ll = new SList();

        ll.insertFront(10);
        ll.insertFront(20);
        ll.insertFront(30);
        ll.insertFront(40);
        ll.insertFront(50);

        System.out.println("\nAt first, the SList is - " + ll.toString()+ ", it's size is - " + ll.length());
        int curSize = ll.length();
        System.out.println("Checking task 1, insertEnd's functionality :\n");
        ll.insertEnd(13);
        ll.insertEnd(97);
        ll.insertEnd(11);
        System.out.println("Inserted " + (ll.length() - curSize)+ " items at the end of SList.");
        System.out.println("Now, the SList is - " + ll.toString()+ ", it's size is - " + ll.length());


        System.out.println("\nChecking task 2, nth(int position)'s functionality : :\n");
        for (int i = -1; i <= ll.length() + 1; i++) {
            System.out.println("The item at " + i +"th position is "+ ll.nth(i));
        }
        // System.out.println(ll.toString());
    }
}
