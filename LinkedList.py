# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 09:54:42 2022

@author: Michael
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n0 = Node(0)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            
    def traverse(self):
        if self.head is not None:
            print(self.head.data)
            n = self.head
            while n.next is not None:
                print(n.next.data)
                n = n.next
        else:
            pass


test = LinkedList()
test.traverse()
test.push(2)
test.push(56)
test.push(3)
test.push(8)
test.traverse()



class LinkedList:
    def __init__(self):
        self.head = None
        
    def push_order(self, new_data):
        new_node = Node(new_data)
        if self.head is not None:
            n = self.head
            if new_node.data <= n.data:
                new_node.next = self.head
                self.head = new_node
            else:
                while n.next is not None and new_node.data > n.next.data:
                    n = n.next
                new_node.next = n.next
                n.next= new_node
        else:
            self.head = new_node
            
    def traverse(self):
        if self.head is not None:
            print(self.head.data)
            n = self.head
            while n.next is not None:
                print(n.next.data)
                n = n.next
        else:
            pass


test = LinkedList()
test.traverse()
test.push_order(2)
test.push_order(56)
test.push_order(3)
test.push_order(8)
test.push_order(0)
test.push_order(-100)
test.push_order(45)
test.traverse()


