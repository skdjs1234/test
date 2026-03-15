dp = [[[[0] * 10 for _ in range(10)] for __ in range(10)] for ___ in range(10)]

print(dp)
### 下面是基于fliter函数和map函数的用法
'''
def is_even(num
):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num
):
    """求平方"""
    return num ** 2


old_nums = [
35, 12, 8, 99, 60, 52
]
new_nums = 
list(map(square, filter
(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]'''


#当然，要完成上面代码的功能，也可以使用列表生成式，列表生成式的做法更为简单优雅。

'''python
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = [num ** 2 for num in old_nums if num % 2 == 0]
print(new_nums)  # [144, 64, 3600, 2704]
'''