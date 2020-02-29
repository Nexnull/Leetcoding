class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def test(self,head):
        while head.next != None:
            print(head.val)
            head = head.next

if __name__ == "__main__":

    solution = Solution()
    solution.test()

