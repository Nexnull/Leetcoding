import sys

class Question(object):
    def question2(self, data):

        data = sorted(data)
        self.res = 0
        print(data)
        self.helper(data, 1, data[0])
        print(self.res)

    def helper(self, data, cur, temp):
        if cur == len(data)-1:
            self.res = max(self.res, len(temp))
            return
        print(temp, data[cur])
        for i in range(cur, len(data)):
            if temp[-1] <= data[i][0]:
                self.helper(data, cur + 1, temp + data[i])


if __name__ == "__main__":
    data = ["aaa","befg","bbb","zzz"]

    question = Question()
    question.question2(data)

    a = ["aaa","befg","bbb","zzz"]
    print(sorted(a))