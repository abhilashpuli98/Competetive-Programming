# Last Updated: 6/22/2026, 12:43:24 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pn=None
        cn=slow.next
        slow.next=None
        while cn:
            nn=cn.next
            cn.next=pn
            pn=cn
            cn=nn
        newHead=pn
        n1,n2=head,newHead
        while n2:
            next1 = n1.next
            next2 = n2.next
            n1.next = n2
            n2.next = next1
            n1 = next1
            n2 = next2


         

