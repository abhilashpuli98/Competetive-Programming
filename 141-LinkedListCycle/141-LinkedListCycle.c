// Last Updated: 6/22/2026, 12:43:30 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
    if(head==NULL || head->next==NULL)
        return 0;
    struct ListNode *slow=head;
    struct ListNode *fast=head->next;
    while(slow!=fast)
    {
        if(fast==NULL || fast->next==NULL)
        {
            return 0;
        }
        slow=slow->next;
        fast=fast->next->next;
    }
    return 1;
}
    