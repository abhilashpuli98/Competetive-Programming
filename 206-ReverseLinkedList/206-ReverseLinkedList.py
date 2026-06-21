# Last Updated: 6/22/2026, 12:42:32 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cn=head
        pn=None
        while cn:
            nn=cn.next
            cn.next=pn
            pn=cn
            cn=nn
        return pn

