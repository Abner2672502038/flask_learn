"""
@program: flask_learn
@author: Abner
@create: 2021-11-25 19:49
"""
# 1.*/** 用于数学运算
# 乘积
a1 = 2 * 2
# 求幂
a2 = 2 ** 3
print(a1)
print(a2)


# 2. */**用于函数形参
# *表示一个元组列表
def test(pa1, *args):
    print("pa1=", pa1)
    print("args=", args)


# **表示一个词典
def test_doubleStar(pa2, **kwargs):
    print("pa2=", pa2)
    print("kwargs=", kwargs)


test(1, 2, 3, 4, 5)
test_doubleStar('param2', p1='1', p2=3, p3=4)


def test_combine(p1, *args, **kwargs):
    print(p1)
    print(args)
    print(kwargs)


test_combine(1,2,3,4,5,k2=2,k3=3)


print("--------------------------------")
# 3. */** 用于函数实参
# 实质是元组的解包和字典解包
a=[1,2,3,4,5]
b={'k1':1,'k2':2,'k3':3}
test_combine(0,*a,**b)

# 4.
s='asddfgg'
print(*s)


print("-------------------------------")
a,b,*c=1,2,3,4
print(c)


