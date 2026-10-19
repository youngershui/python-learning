def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)
def person2(name,age,**kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:',name,'age:',age,'other',kw)#可以自由接受其余关键字参数
def person3(name,age,*,city,job):
        #*后面的必须写成city=****关键字形式
    print('name:',name,'age',age,'city',city,'job',job)
def person4(name,age,*city,job):
    print('name:',name,'age',age,'city',city,'job',job)
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person5(a,b,c,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args =', args,'kw=',kw)
def person6(a,b,c,*d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
def mul(x, y):
    return x * y

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

