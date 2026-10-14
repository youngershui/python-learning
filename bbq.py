import math
def quadratic(a,b,c):
    delta = b**2-4*a*c
    sqrt_delta = math.sqrt(delta)
    x1= (-b+sqrt_delta)/(2*a)
    x2= (-b-sqrt_delta)/(2*a)
    return(x1,x2)
#测试
print('quadratic(2,3,1)=', quadratic(2,3,1))
print('quadratic(1,3,-4)=', quadratic(1,3,-4))
if quadratic(2,3,1)!= (-0.5,-1.0):
    print('测试失败')
elif quadratic(1,3,-4)!= (1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')