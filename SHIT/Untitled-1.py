class C:
    def init(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y

# 创建实例并调用方法
obj = C(3, 5)
print(obj.add())  # 输出 8
print(obj.mul())  # 输出 15

obj.__dict__
obj2 =C(4, 6)
print(obj2.add())  # 输出 10
print(obj2.mul())  # 输出 24
obj2.__dict__
