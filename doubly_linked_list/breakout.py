# How do you find and return the middle node of a singly linked list in one pass? 
# You do not have access to the length of the list. 
# If the list is even, you should return the first of the two "middle" nodes. 
# You may not store the nodes in another data structure.

class LinkedList():
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def find_middle_node(node):
        #if the list is even return first of the two 
        count = 0
        faster_node = node

        while(faster_node !=None):
            

# How do you reverse a singly linked list without recursion? 
# You may not store the list, or it's values, in another data structure.


class ListNode():

    def __init__(self,x):
        self.val = x
        self.next = None


    def reverse(node):
        pre = None
        while node != None:
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        return pre
