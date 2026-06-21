# Last Updated: 6/22/2026, 12:45:44 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=total=0
        head=l1
        while l1 or l2:
            total=carry
            if l1:
                total+=l1.val
            if l2:
                total+=l2.val
                l2=l2.next
            num=total%10
            carry=total//10
            if l1:
                l1.val=num
                prev=l1
                l1=l1.next
            else:
                prev.next=ListNode(num)
                prev=prev.next
        if carry:
            prev.next=ListNode(carry)
        return head
