x=10
y=3
z=x/y  # 在执行除法运算的时候，将赋值的结果赋值给z
print(z,type(z))  # 隐式转换，通过运算隐式的转换结果的类型

#float类型转成int类型，只保留整数部分
print('float类型转换成int类型:',int(3.14))
print('float类型转换成int类型:',int(3.9))
print('float类型转换成int类型:',int(-3.14))
print('float类型转换成int类型:',int(-3.9))

#将int类型转成float类型
print('将int转换成float类型:',float(10))
#将str类型转成int类型
print(int('100')+int('200'))
#将字符串转成int或float时报错的情况
#print(int('18a'))  # 是因为a不是十进制的数
#print(int('3.14'))  #是因为有小数点
#print(int('45a.987'))  #是因为有小数点和字母

#chr()ord()是一对互为相反数
print(ord('杨')) # 杨在unicode表中对应的整数值
print((chr(26472)))  # 26472整数在unicode表中对应的字符是什么

#进制之间的转换操作
