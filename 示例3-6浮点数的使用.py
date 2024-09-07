height=187.6  # 身高
print(height)
print(type(height))  # type()查看height这个变量的数据问题

x=10
y=10.0
print('x的数据类型：',type(x))  # x的数据类型： <class 'int'> （int是函数取整类型）
print ('y的数据类型：',type(y))  # y的数据类型： <class 'float'>  （float是浮点类型）

x=1.99e1413
print('科学计数法:',x,'x的数据类型:',type(x))
print(0.1+0.2)  # 不确定的尾数问题0.30000000000000004

#整数是Python当中的不可变数据类型
#浮点数也是Python当中的不可变数据类型
print(round(0.1+0.2,1))   # 0.3