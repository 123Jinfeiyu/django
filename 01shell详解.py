"""
shell: 用户和操作内核的交互工具。


知名的shell：

Bourne Shell（/usr/bin/sh或/bin/sh）
Bourne Again Shell（/bin/bash）
C Shell（/usr/bin/csh）
K Shell（/usr/bin/ksh）


如何去判断操作系统使用的是哪个shell：
echo  $SHELL

编程语言基本要素：

1、变量
变量定义的规则：
1、只能包含字母、数字和下划线(区分大小写)
2、不能一数字开头
3、避免使用shell关键字
4、避免使用空格

5、使用大写来表示常量(习惯)
6、避免使用特殊符号

正确的写法：
name="罗建斌"

错误的写法：
name = "罗建斌"

输出变量：
echo $变量名称


2、数据类型

一、字符串
使用单引号或者双引号来定义字符
string1='my first shell script!'
string2="my second shell script!"

单引号不会解析变量，可以双引号可以


获取字符串的长度

string1='my first shell script!'
echo ${#string1}

截取部分字符串：

string1='my first shell script!'
echo ${string1:0:2}  # 内容：开始位置：长度


二：数组(等价于Python的列表+字典)
普通数组：
students=("程序员小新" "友谊帅哥" "小骆")  # 元素于元素之间使用空格分隔

添加元素：
students[3]="一大口"
读取数组：
students[0]
获取数组长度
${#students[@]}

3、运算符
算术运算符：+ - *  / %

bash不支持简单的数学运算需要借助其他命令工具比如 expr
a=10
b=10

echo `expr $a + $b`


比较运算符：
-eq:等于
-ne:不等于
-gt:大于
-lt: 小于
-ge:大于等于
-le:小于等于







4、流程控制
if判断：
if 判断
then
    代码
    代码
    代码
elif 判断
then
    代码
    代码
else
    代码
    代码
fi



5、函数







"""


