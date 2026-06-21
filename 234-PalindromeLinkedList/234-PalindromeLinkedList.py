# Last Updated: 6/22/2026, 12:42:04 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        cn=slow
        while cn:
            nn=cn.next
            cn.next=prev
            prev=cn
            cn=nn
        trv=head
        while prev and trv:
            if prev.val!=trv.val:
                return False
            prev=prev.next
            trv=trv.next
        return True