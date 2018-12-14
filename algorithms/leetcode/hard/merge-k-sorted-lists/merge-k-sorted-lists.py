class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        list1 = lists[0]
        list2 = lists[1]
        head = self.merge2Lists(list1, list2)
        self.printList(head)

    def merge2Lists(self, list1, list2):
        head1 = list1
        head2 = list2
        head = None
        if head1.val > head2.val:
            head = head2
            head2 = head2.next
        else:
            head = head1
            head1 = head1.next

        while head2 != None and head1 != None:
            if head1.val >= head2.val:
                head.next = head2
                head2 = head2.next
            elif head2.val > head1.val:
                head.next = head1
                head1 = head1.next

        return head

    def printList(self, list):
        while list != None:
            print(list.val)
            list = list.next

solution = Solution()

# create list 1
listnode = None
lastnode = None

list1 = ListNode(0)
lastnode = list1
for i in range(0, 9):
    listnode = ListNode(i)
    if lastnode != None:
        lastnode.next = listnode
    lastnode = listnode

list2 = ListNode(0)
lastnode = list2
for i in range(0, 4):
    listnode = ListNode(i*3)
    if lastnode != None:
        lastnode.next = listnode
    lastnode = listnode

list3 = ListNode(0)
lastnode = list3
for i in range(0, 3):
    listnode = ListNode(i + 2)
    if lastnode != None:
        lastnode.next = listnode
    lastnode = listnode

lists = [list1, list2, list3]
solution.mergeKLists(lists)

