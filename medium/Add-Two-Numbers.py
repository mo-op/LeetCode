# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def read_ll(self, node: ListNode) -> list:
        ans = [node.val]
        if node.next:
            ans += self.read_ll(node.next)
        return ans
    
    def ll_to_int(self,node: ListNode) -> int:
        node_digits = self.read_ll(node)
        return int(''.join(str(n) for n in reversed(node_digits)))
    
    def int_to_ll(self, num: int) -> ListNode:
        previous = None
        for n in str(num):
            current = ListNode(n)
            if previous:
                current.next = previous
            previous = current
        return previous
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_int = self.ll_to_int(l1)
        l2_int = self.ll_to_int(l2)
        return self.int_to_ll(l1_int + l2_int)
        
