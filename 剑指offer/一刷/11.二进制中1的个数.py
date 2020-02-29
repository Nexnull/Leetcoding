class Solution:
    def NumberOf1(self, n):
        res = 0
        for i in range(32):
            if (n>>i & 1) == 1:
                res += 1

        print(res)
        return res




if __name__ == "__main__":
    solution = Solution()
    solution.NumberOf1(3)


"""
答案：
1.int 占据4个bytes, 32个bits 所以for i in range(32)
2.
    111
  & 001
  ------ 
      1

    110
  & 001
  ------
      0
      
    所以假如说最后一位是0，则出结果0，是1，则出结果1。每次执行都
    把n往右挪一位 >>1。以此判断每一位
    
3. 当确认最后一位为1时 ，res += 1

  

"""