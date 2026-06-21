// Last Updated: 6/22/2026, 12:42:37 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode node;
struct ListNode* reverseList(struct ListNode* head) {
    node *pn=NULL;
    node *cn=head;
    node *nn=head;
    while(cn!=NULL){
        nn=nn->next;
        cn->next=pn;
        pn=cn;
        cn=nn;  
    }
    return pn;
    
}