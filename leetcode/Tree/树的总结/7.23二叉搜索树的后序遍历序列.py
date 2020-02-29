class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        return self.helper(sequence)

    def helper(self,sequence):
        if len(sequence) == 0:
            return True

        root = sequence[-1]
        flag = -1

        for left_value in sequence:
            if left_value > root:
                flag = sequence.index(left_value)
                break

        for right_value in sequence[flag:]:
            if right_value < root:
                return False

        return self.helper(sequence[:flag]) and self.helper(sequence[flag:-1])









"""
后序遍历：left , right , root
等等，在我迷茫的时候，要始终想起BST的特征 left < root < right 
所以我们只要递归对比，那些元素是否确实满足left < root < right 就可以了

然后这里的递归处理也是挺有意思的：
把每一次的判断都放在helper里面做，
当列表长度为0时，返回true
列表的最后一个元素为root
然后走一个从前往后的循环，发现比root大的元素就停止，并记录index(说明到了right)
然后从这个index继续走，发现比root小的元素就返回false,因为right 不可能小于root
最后递归的时候，不把root放进递归，达到sequence长度递减的效果

"""