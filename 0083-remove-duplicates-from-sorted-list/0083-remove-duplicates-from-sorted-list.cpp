class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr)
            return head;

        ListNode* newHead = new ListNode(head->val);
        ListNode* tail = newHead;
        ListNode* curr = head->next;

        while (curr != nullptr) {
            if (tail->val != curr->val) {
                tail->next = new ListNode(curr->val);
                tail = tail->next;
            }

            curr = curr->next;
        }

        return newHead;
    }
};