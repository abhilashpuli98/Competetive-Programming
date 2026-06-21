# Last Updated: 6/22/2026, 12:43:09 AM
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return 
        t1=headA
        t2=headB
        while headA!=headB:
            headA=headA.next if headA else t2
            headB=headB.next if headB else t1
        return headA