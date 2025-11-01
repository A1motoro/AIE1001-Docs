# AIE1001 期中复习 - 英文术语词汇表

本文档列出了期中复习报告中出现的英文术语及其中文翻译，帮助理解课程内容。

## 基础概念

- **Interpreter** - 解释器：直接执行代码的程序，无需先编译
- **Compiler** - 编译器：将源代码转换为机器码的程序
- **Interactive Mode** - 交互模式：逐行输入代码并立即执行
- **Script Mode** - 脚本模式：将代码保存在文件中然后执行
- **Variable** - 变量：内存中的命名空间，用于存储数据
- **Constant** - 常量：固定不变的值
- **Reserved Words** - 保留字：Python 语言中不能用作变量名的关键字（如 def, if, while）
- **Data Type** - 数据类型：数据的分类（如 int, float, str）

## 数据类型相关

- **Integer (int)** - 整数：整数值，如 1, 2, -3
- **Float** - 浮点数：小数值，如 3.14, 2.5
- **String (str)** - 字符串：文本数据，如 'hello', "world"
- **Boolean (bool)** - 布尔类型：逻辑值，True 或 False
- **Falsy** - 假值：在布尔上下文中被视为 False 的值（如 0, "", [], None）
- **Truthy** - 真值：在布尔上下文中被视为 True 的值

## 运算符和表达式

- **Operator** - 运算符：用于执行运算的符号（如 +, -, *, /）
- **Operand** - 操作数：运算符作用的对象
- **Expression** - 表达式：计算并返回值的代码
- **Precedence** - 优先级：运算符执行的先后顺序
- **Floor Division (//)** - 向下取整除法：向负无穷方向取整
- **Exponentiation (**)** - 幂运算：如 2**3 = 8
- **Concatenation** - 连接：将字符串或列表连接在一起

## 流程控制

- **Comparison Operator** - 比较运算符：用于比较的运算符（==, !=, <, >, <=, >=）
- **Lexicographical** - 字典序：按字母顺序比较
- **ASCII Code** - ASCII 码：字符编码标准
- **Unicode** - Unicode：通用字符编码标准
- **Conditional Statement** - 条件语句：根据条件执行不同代码（if, elif, else）
- **Loop** - 循环：重复执行代码
- **Indefinite Loop** - 不定循环：条件为 False 时停止的循环（while）
- **Definite Loop** - 定循环：遍历序列的循环（for）
- **Iteration** - 迭代：循环中的一次执行
- **Iteration Variable** - 迭代变量：循环中变化的变量
- **Break** - 中断：退出循环
- **Continue** - 继续：跳过本次迭代，继续下一次

## 函数相关

- **Function** - 函数：可重用的代码块
- **Function Definition** - 函数定义：使用 def 关键字定义函数
- **Function Signature** - 函数签名：函数名和参数数量
- **Parameter** - 参数：函数定义中的变量
- **Argument** - 参数：调用函数时传入的值
- **Return Value** - 返回值：函数返回的结果
- **Void Function** - 无返回值函数：不返回值的函数
- **Fruitful Function** - 有返回值函数：返回值的函数
- **Scope** - 作用域：变量可访问的范围
- **Local Variable** - 局部变量：函数内定义的变量
- **Global Variable** - 全局变量：函数外定义的变量
- **Default Argument** - 默认参数：函数参数的默认值

## 数据结构

- **List** - 列表：可变的序列，用方括号 []
- **Dictionary (dict)** - 字典：键值对集合，用花括号 {}
- **Tuple** - 元组：不可变的序列，用圆括号 ()
- **Sequence** - 序列：有序的数据集合
- **Mutable** - 可变的：可以修改的数据结构
- **Immutable** - 不可变的：不能修改的数据结构
- **Index** - 索引：访问序列元素的位置（从 0 开始）
- **Slice** - 切片：获取序列的一部分
- **Key** - 键：字典中用于查找值的标识符
- **Value** - 值：字典中与键对应的数据
- **Key-Value Pair** - 键值对：字典中的一个条目

## 字典相关方法

- **get()** - 获取方法：安全地获取字典值，键不存在时返回默认值
- **keys()** - 键方法：返回字典的所有键
- **values()** - 值方法：返回字典的所有值
- **items()** - 项方法：返回字典的所有键值对

## 列表相关方法

- **append()** - 追加方法：在列表末尾添加元素
- **sort()** - 排序方法：原地排序列表
- **sorted()** - 排序函数：返回排序后的新列表
- **len()** - 长度函数：返回序列的长度
- **range()** - 范围函数：生成数字序列

## 递归相关

- **Recursion** - 递归：函数调用自身
- **Recursive Definition** - 递归定义：包含递归的数学或程序定义
- **Base Case** - 基例：递归中无需递归的简单情况
- **Recursive Case** - 递归例：递归中需要递归的复杂情况
- **Activation Record** - 激活记录：函数调用时创建的记录，存储参数和局部变量
- **Frame** - 帧：激活记录的另一种称呼
- **Call Stack** - 调用栈：存储函数调用信息的栈结构
- **Stack Overflow** - 栈溢出：递归深度过深导致的错误
- **Linear Recursion** - 线性递归：每次调用最多进行一次递归调用
- **Multiple Recursion** - 多重递归：每次调用进行两次或更多递归调用
- **Binary Search** - 二分搜索：对有序列表的递归搜索算法
- **Factorial** - 阶乘：n! = n × (n-1) × ... × 1

## 数制相关

- **Decimal** - 十进制：基数为 10 的数制
- **Binary** - 二进制：基数为 2 的数制
- **Octal** - 八进制：基数为 8 的数制
- **Hexadecimal** - 十六进制：基数为 16 的数制
- **Positional Notation** - 位置记数法：根据位置表示数值的方法
- **Base** - 基数：数制的基础数字
- **Bit** - 位：二进制数字（0 或 1）
- **Byte** - 字节：8 位

## 计算机基础

- **Von Neumann Architecture** - 冯·诺伊曼架构：现代计算机的基本架构
- **CPU** - 中央处理器：计算机的核心处理单元
- **Control Unit (CU)** - 控制单元：CPU 中负责获取指令的部分
- **Arithmetic Logic Unit (ALU)** - 算术逻辑单元：CPU 中负责执行运算的部分
- **Memory** - 内存：存储数据和程序的地方
- **RAM** - 随机存取存储器：易失性内存
- **ROM** - 只读存储器：非易失性内存
- **Input Device** - 输入设备：键盘、鼠标等
- **Output Device** - 输出设备：显示器、打印机等

## 异常处理

- **Exception** - 异常：程序运行时发生的错误
- **Try/Except** - 尝试/异常：捕获和处理异常的语句
- **Error** - 错误：程序中的问题
- **KeyError** - 键错误：访问字典中不存在的键时发生的错误
- **TypeError** - 类型错误：类型不匹配导致的错误
- **ValueError** - 值错误：值不正确导致的错误

## 其他重要术语

- **Syntax Error** - 语法错误：代码不符合 Python 语法规则
- **Indentation** - 缩进：Python 中用于表示代码块的空格或制表符
- **Assignment** - 赋值：将值赋给变量
- **Cascaded Assignment** - 级联赋值：一次给多个变量赋相同值
- **Simultaneous Assignment** - 同时赋值：一次给多个变量赋不同值
- **Evaluation** - 求值：计算表达式的值
- **String Literal** - 字符串字面量：直接在代码中写的字符串
- **List Comprehension** - 列表推导：创建列表的简洁方式
- **Environment Diagram** - 环境图：可视化变量和函数调用的图
- **Python Tutor** - Python 可视化工具：用于可视化代码执行

## 考试相关

- **Single Choice** - 单选题：只有一个正确答案的选择题
- **Multiple Choice** - 多选题：有多个正确答案的选择题
- **Short Answer Question** - 简答题：需要写代码或解释的题目
- **Code Fault Localization** - 代码故障定位：找出代码中的错误
- **Code Completion** - 代码补全：填写代码中的空白部分
- **Function Design** - 函数设计：设计并实现函数

