"""
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
这题是正序求的 ， 不像第一题是倒叙，可以直接加，这里需要处理一下，把正序变成倒叙
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        cur = ListNode(0)

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        while stack1 != [] or stack2 != []:
            if stack1 == []:
                digit_sum = stack2.pop()
            elif stack2 == []:
                digit_sum = stack1.pop()
            else:
                digit_sum = stack1.pop() + stack2.pop()

            digit_sum += carry
            carry = 0

            if digit_sum >= 10: carry = digit_sum // 10

            cur.val = digit_sum % 10
            nex = ListNode(0)
            nex.next = cur
            cur = nex

        if carry != 0:
            cur.val = carry

        return cur.next if carry == 0 else cur

# 7243   3427
#  564   465
# 7807   7087
"""
https://leetcode.com/problems/add-two-numbers-ii/discuss/129192/clear-python-solution-using-stack
答案：
其实这题一切都和第二题非常像，但是有些特殊的地方需要处理下
1.这题因为链表的顺序和我们要求解的顺序不一样，所以我们要先把两个链表给放进stack
2.然后当两个stack都不为空的时候，我们要依次把stack里面最上面的元素（最低位）给pop出来，相加成sum
3. sum的处理依旧是 sum %10 ，因为我们只要个位
   进位依旧是carry, 当sum >= 10的时候 carry //= 10, 注意，当carry成功给sum附值以后，记得清0，避免影响下次
   
4.到了最关键的部分 
    7243   3427
     564   465
    7807   7087
  假如说我们正序来添加node, 出来的结果是7-0-8-7，与正确答案是相反的，所以我们添加node的时候，要反向加
  例如 cur = 7
  next = new node 我们要让 next->cur, 再把cur = next
  使得 0 -> 7
       |
       cur
  这样一次次创建一个新node放在已有node的前面

5. 当遇到【5】【5】的情况，我们会带着carry = 1退出循环，记得在循环外判断下carry
"""