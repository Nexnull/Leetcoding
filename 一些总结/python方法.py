


#some python tricky

#56. 按照要求来排序列表里的列表
















#=============================================
lambda:

语法形式：lambda argument_list: expression

用法：
1。将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。

    add=lambda x, y: x+y
    执行add(1,2)，输出为3。


2.将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换
3.将lambda函数作为其他函数的返回值，返回给调用者。

4.
filter函数。此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。

sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。

map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，其结果[2, 3, 4]。

reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。


原文链接：https://blog.csdn.net/zjuxsl/article/details/79437563



enumerate：


if else:一行表达式
为真时放if前
c = a if a>b else b


#https://blog.csdn.net/qwe1257/article/details/83272340
collections.Counter

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print (dict(c))
#{'red': 2, 'blue': 3, 'green': 1}



filter函数
起到过滤作用，把需要过滤的东西储存到b中
a = [11, 20, 4, 5, 16, 28]
b = filter(lambda x: x % 2 != 0, a)


python max,min的一些技巧
https://www.cnblogs.com/whatisfantasy/p/6273913.html
