import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Question(object):
    def question2(self, root, n):

        self.res = []
        self.helper(root, n, [])

        # for _ in range(len(self.res)):
        #     print(_+1, self.res[_])
        # print(n ,len(self.res))

        for n in range(1,11):
            self.helper(root, n, [])
            print(n ,len(self.res))
            self.res = []




    def helper(self, root, n, temp):
        if root.val == "E":
            if n == 0:
                if temp not in self.res:
                    self.res.append(temp + ["E"])
                return
            else:
                return

        if n <= 0:
            return

        self.helper(root.left, n - 1, temp + [root.val])
        self.helper(root.right, n - 1, temp + [root.val])




if __name__ == "__main__":
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")
    G = TreeNode("G")
    H = TreeNode("H")

    A.left = H; A.right = B
    B.left = A; B.right = C
    C.left = B; C.right = D
    D.left = C; D.right = E
    E.left = D; E.right = F
    F.left = E; F.right = G
    G.left = F; G.right = H
    H.left = G; H.right = A

    question = Question()
    question.question2(A, 1)
