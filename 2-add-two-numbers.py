# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []
        item1, item2 = l1, l2
        
        while item1:
            list1.append(item1.val)
            item1 = item1.next
        while item2:
            list2.append(item2.val)
            item2 = item2.next
        
        list1, list2 = list1[::-1], list2[::-1]
        
        integer1 = int(''.join(map(str, list1)))
        integer2 = int(''.join(map(str, list2)))
        
        int_list = list(map(int, str(integer1 + integer2)))
        
        link_list = None
        
        int_list = int_list[::-1]
        
        for i in int_list:
            new_node = ListNode(i)
            if link_list is None:
                link_list = new_node
            else:
                temp = link_list
                while temp.next != None:
                    temp = temp.next
                temp.next = new_node
        return link_list
