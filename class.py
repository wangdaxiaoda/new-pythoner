class Quan:
    # 构造函数
    def __init__(self, base=1, continueTime=0, graw=0.1):
        self.base = base
        self.continueTime = continueTime
        self.graw = graw

    # self 类似于 this，但是函数声明时需要默认带上这个参数
    def get_res(self):
        return self.base + self.continueTime * self.graw

    def add_time(self, c_time):
        self.continueTime += c_time


c1 = Quan(continueTime=1, graw=3)

print(c1.get_res())
c1.add_time(5)
print(c1.get_res())

# 继承：类的继承

# 方式1: 直接通过添加属性来实现继承


# class Quan1(Quan):
#     is_good = False

#     def judge_state(self, baseline):
#         self.is_good = self.base > baseline


# cq1 = Quan1(2)
# cq1.judge_state(1.5)
# print(cq1.is_good)

# 方式2: 重新定义构造函数


# class Quan2(Quan):
#     def __init__(self, is_good=False, base=3, graw=0.5):
#         self.is_good = is_good
#         # 函数调用的时候，如果不按顺序传入参数，则需要指定变量名
#         super().__init__(base, graw=graw)

#     def judge_state(self, baseline):
#         self.is_good = self.base > baseline


# cq2 = Quan2(graw=3)
# cq2.judge_state(2)
# print(cq2.is_good, cq2.continueTime, cq2.graw)  # True 0 3

# var.add(5)
