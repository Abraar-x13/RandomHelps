package com.codeKat;

public class SListNode {

    public Object item;
    public SListNode next;

    public SListNode(Object o, SListNode n) {
        item = o;
        next = n;
    }

    public SListNode(Object o) {
        item = o;
        next = null;
    }

}
