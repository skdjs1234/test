def counter(a=1):  # a是默认步长，默认值1
    current = 0    # 计数器初始值（固定为0，若想自定义可再加参数）
    def inner():
        nonlocal current
        current += a  # 用参数a代替硬编码的1，发挥步长作用
        return current  # 返回更新后的计数值，才能打印出结果
    return inner

# 测试效果
c1 = counter()     # 默认步长1
print(c1())  # 输出 1 (0+1)
print(c1())  # 输出 2 (1+1)

c2 = counter(3)    # 自定义步长3
print(c2())  # 输出 3 (0+3)
print(c2())  # 输出 6 (3+3)
