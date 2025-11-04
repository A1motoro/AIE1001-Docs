# Python 面向对象编程（OOP）详解

本文档基于 AIE1001 课程第 7-9 周内容，详细讲解 Python 中的面向对象编程语法、用法和扩展知识。

## 目录
1. [基础概念](#基础概念)
2. [类的定义](#类的定义)
3. [构造函数和self](#构造函数和self)
4. [访问对象成员](#访问对象成员)
5. [可变对象与不可变对象](#可变对象与不可变对象)
6. [数据隐藏（私有字段）](#数据隐藏私有字段)
7. [抽象和封装](#抽象和封装)
8. [继承](#继承)
9. [方法重写](#方法重写)
10. [多态和动态绑定](#多态和动态绑定)
11. [object类及其方法](#object类及其方法)
12. [多继承](#多继承)

---

## 基础概念

### 对象（Object）
- **定义**：对象代表现实世界中可以明确识别的实体
- **示例**：学生、桌子、圆形、按钮、贷款等
- **三个关键要素**：
  - **Identity（身份）**：唯一标识符，Python 自动为每个对象分配唯一的 id
  - **State（状态）**：对象内部存储的数据，描述对象的属性
  - **Behavior（行为）**：对象可以执行的操作，通过方法定义

### 类（Class）
- **定义**：类是用来创建对象的蓝图或模板
- **类比**：类与对象的关系类似于苹果派配方与苹果派的关系
- **包含**：
  - **数据字段（Data Fields）**：存储信息的变量
  - **方法（Methods）**：执行操作的函数

### 实例（Instance）
- **定义**：对象是类的实例，创建对象的过程称为实例化（instantiation）
- **特点**：一个类可以创建多个实例，每个实例有自己独立的数据

### 为什么需要OOP？
1. **代码组织（模块化）**：将大程序分解为类，每个类处理一种类型的事物
2. **代码复用**：创建类后可以创建多个对象，无需重复编写代码
3. **易于维护**：数据和操作封装在一起，修改时不影响其他部分
4. **建模现实世界**：用代码表示现实世界的事物，更符合问题本身的结构

---

## 类的定义

### 基本语法
```python
class 类名:
    def __init__(self, 参数1, 参数2, ...):
        # 初始化数据字段
        self.数据字段1 = 参数1
        self.数据字段2 = 参数2
    
    def 方法名(self, 参数):
        # 方法体
        pass
```

### 示例：Circle类
```python
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
        self.fillColor = 'blue'
    
    def getArea(self):
        return 3.14159 * self.radius * self.radius
```

### 关键点
- **类名**：通常首字母大写（驼峰命名法）
- **内置类 vs 自定义类**：
  - 内置类：Python 预定义的类（如 `str`, `int`, `list`, `dict`, `tuple`）
  - 自定义类：自己创建的类

---

## 构造函数和self

### `__init__()` 方法
- **作用**：初始化新对象的状态
- **调用时机**：创建对象时自动调用
- **特殊方法**：又称为初始化器（initializer）

### self 参数
- **定义**：所有方法（包括初始化器）的第一个参数必须是 `self`
- **作用**：`self` 指向调用方法的对象
- **注意**：
  - 在 `__init__()` 中，`self` 自动指向刚创建的对象
  - 调用方法时不需要传递 `self`，Python 自动传递
  - 在类内部访问数据字段和方法时，必须使用 `self.`

### self 的作用域
- **实例变量**：通过 `self.变量名` 定义的变量，作用域是整个类
- **局部变量**：在方法内部定义的变量（不使用 `self.`），作用域仅限于该方法

### 示例
```python
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius      # 实例变量，整个类可用
        self.fillColor = 'blue'
    
    def getArea(self):
        pi = 3.14159              # 局部变量，只在getArea中可用
        return pi * self.radius * self.radius
```

### 创建对象（构造函数调用）
```python
# 创建对象时，构造函数做两件事：
# 1. 在内存中为类创建对象
# 2. 调用类的 __init__() 方法初始化对象

circle1 = Circle(3.0)    # 传入 radius=3.0
circle2 = Circle()        # 使用默认值 radius=1.0
circle3 = Circle(5.0)    # 传入 radius=5.0
```

### 构造函数参数匹配
- 构造函数的参数必须与 `__init__()` 方法的参数（不包括 `self`）匹配
- 如果 `__init__()` 中有默认参数，构造函数可以不传参

---

## 访问对象成员

### 点运算符（.）
- **作用**：访问对象的数据字段和调用方法
- **语法**：`对象.成员名`
- **示例**：
```python
circle = Circle(3.0)
print(circle.radius)        # 访问数据字段
circle.fillColor = 'red'    # 修改数据字段
area = circle.getArea()     # 调用方法
```

### 数据字段（Data Fields）
- **别名**：实例变量（instance variables）
- **特点**：每个对象（实例）有自己独立的数据字段值
- **访问**：`对象.数据字段名`

### 方法（Methods）
- **别名**：实例方法（instance methods）
- **特点**：方法由对象调用，基于该对象的数据字段执行操作
- **调用**：`对象.方法名(参数)`

### 示例：TV类
```python
class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
    
    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = False
    
    def setChannel(self, newChannel):
        if 1 <= newChannel <= 120:
            self.channel = newChannel
    
    def setVolume(self, newVolumeLevel):
        if 0 <= newVolumeLevel <= 7:
            self.volumeLevel = newVolumeLevel

# 使用
tv1 = TV()
tv1.turnOn()
tv1.setChannel(30)
tv1.setVolume(3)

tv2 = TV()
tv2.turnOn()
tv2.setChannel(50)
# tv1 和 tv2 有各自独立的 channel、volumeLevel 等
```

---

## 可变对象与不可变对象

### 可变对象（Mutable Objects）
- **定义**：可以修改内容而不改变其身份的对象
- **类型**：
  - 列表（list）
  - 字典（dict）
  - 用户定义的对象（如果其属性可以修改）
- **示例**：
```python
numbers = [1, 2, 3]
numbers[0] = 10           # 修改元素
print(numbers)            # [10, 2, 3]
# 对象 identity 不变，但内容变了
```

### 不可变对象（Immutable Objects）
- **定义**：创建后内容不能改变的对象；任何修改都会创建新对象
- **类型**：
  - 整数（int）
  - 浮点数（float）
  - 字符串（str）
  - 元组（tuple）
- **示例**：
```python
name = "Alice"
name = name.replace("A", "M")  # 返回新字符串 "Mlice"
# 原字符串 "Alice" 未改变，name 现在指向新字符串
```

### 用户定义对象的可变性
```python
class Count:
    def __init__(self, count=0):
        self.count = count

c = Count()
c.count = 5              # 修改对象的数据字段
# 对象 identity 不变，但状态改变了
```

### 重要区别
- **可变对象**：修改内容时，对象本身不变（同一个 id）
- **不可变对象**：修改时会创建新对象（新的 id）

---

## 数据隐藏（私有字段）

### 为什么需要数据隐藏？
1. **数据可能被篡改**：直接访问数据字段不安全
2. **难以维护**：类的实现变更时，直接访问会导致大量代码需要修改
3. **易出错**：不规范的访问可能导致 bug

### 私有数据字段
- **定义**：在 Python 中，私有数据字段使用**两个前导下划线**（`__`）定义
- **访问限制**：私有字段和方法只能在类内部访问，不能在类外部访问
- **语法**：`self.__私有字段名`

### 示例：私有字段
```python
class Circle:
    def __init__(self, radius=1.0):
        self.__radius = radius        # 私有字段
        self.fillColor = 'blue'       # 公有字段
    
    def getRadius(self):              # getter 方法
        return self.__radius
    
    def setRadius(self, radius):     # setter 方法
        if radius > 0:
            self.__radius = radius

circle = Circle(3.0)
print(circle.__radius)    # 错误！AttributeError: 'Circle' object has no attribute '__radius'
print(circle.getRadius()) # 正确：3.0
circle.setRadius(5.0)     # 正确：通过方法修改
```

### Getter 和 Setter 方法
- **目的**：提供受控的访问接口来访问和修改私有字段
- **Getter**：返回私有字段的值
- **Setter**：设置私有字段的值（可以添加验证逻辑）

### 示例：带验证的 Setter
```python
class Stock:
    def __init__(self, symbol, name, previousPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousPrice
        self.__currentPrice = currentPrice
    
    def getCurrentPrice(self):
        return self.__currentPrice
    
    def setCurrentPrice(self, price):
        if price > 0:                  # 验证逻辑
            self.__currentPrice = price
        else:
            print("Price must be positive!")
```

---

## 抽象和封装

### 抽象（Abstraction）
- **定义**：将代码的实现与其使用分离
- **函数抽象**：将函数的实现与其使用分离
- **类抽象**：将类的实现与其使用分离
- **好处**：使代码易于维护、调试和复用

### 封装（Encapsulation）
- **定义**：将数据和方法组合成单个对象，并向用户隐藏数据字段和方法实现
- **类比**：计算机的封装（隐藏内部实现：CPU、ROM、硬盘）和抽象（公开接口：显示器、键盘、鼠标、电源按钮）

### 类的契约（Contract）
- **定义**：类的公共方法集合及其预期行为描述
- **作用**：用户只需要知道如何调用方法，不需要知道内部实现细节

### 示例：BMI类
```python
class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    
    def getBMI(self):
        bmi = self.__weight / (self.__height ** 2)
        return round(bmi * 100) / 100
    
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

# 使用（不需要知道内部实现）
person = BMI("John", 25, 70, 1.75)
print(person.getBMI())      # 使用公共接口
print(person.getStatus())   # 内部实现被封装
```

---

## 继承

### 基本概念
- **定义**：从现有类定义新类的能力
- **目的**：代码复用，扩展面向对象编程的能力
- **关系**：
  - **父类（Superclass）**：被继承的类，也称为基类（base class）
  - **子类（Subclass）**：继承自父类的类，也称为派生类（derived class）

### 继承语法
```python
class 子类名(父类名):
    def __init__(self, 参数):
        super().__init__(父类参数)  # 调用父类构造函数
        # 子类特有的初始化
    
    # 子类特有的方法和数据字段
```

### 示例：继承GeometricObject
```python
class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.color = color
        self.filled = filled
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
    
    def isFilled(self):
        return self.filled
    
    def setFilled(self, filled):
        self.filled = filled
    
    def __str__(self):
        return f"color: {self.color}, filled: {str(self.filled)}"

class Circle(GeometricObject):
    def __init__(self, radius=1.0, color="green", filled=True):
        super().__init__(color, filled)  # 调用父类构造函数
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    
    def getArea(self):
        return 3.14159 * self.__radius * self.__radius
    
    def getPerimeter(self):
        return 2 * 3.14159 * self.__radius

class Rectangle(GeometricObject):
    def __init__(self, width=1.0, height=1.0, color="green", filled=True):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height
    
    def getArea(self):
        return self.__width * self.__height
    
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
```

### 继承的特点
1. **子类继承父类的所有可访问的数据字段和方法**
2. **子类可以有自己的数据字段和方法**（扩展）
3. **子类不是父类的子集**，通常包含更多信息和方法
4. **继承建模 is-a 关系**：子类是父类的特殊类型
   - Circle is-a GeometricObject ✓
   - Tree is-a Person ✗（不应该用继承）

### 使用super()调用父类方法
```python
class Circle(GeometricObject):
    def __str__(self):
        return f"Circle: {super().__str__()}, radius: {self.__radius}"
```

---

## 方法重写

### 定义
- **方法重写（Method Overriding）**：子类修改父类中定义的方法的实现
- **目的**：为子类提供更具体的实现

### 示例：重写__str__方法
```python
class GeometricObject:
    def __str__(self):
        return f"color: {self.color}, filled: {str(self.filled)}"

class Circle(GeometricObject):
    def __str__(self):
        # 重写父类的 __str__ 方法
        return f"Circle: color={self.color}, filled={self.filled}, radius={self.__radius}"
    
    def printCircle(self):
        # 调用父类的 __str__ 方法
        print(super().__str__())
```

### 要点
- 子类可以重写父类的方法
- 子类中可以使用 `super().方法名()` 调用父类的方法
- 重写的方法必须与父类方法有相同的签名（参数列表）

---

## 多态和动态绑定

### 多态（Polymorphism）
- **定义**：子类的对象可以传递给父类类型的参数
- **含义**：同一个接口可以处理不同类型的对象
- **好处**：代码更通用、更灵活

### 动态绑定（Dynamic Binding）
- **定义**：Python 在运行时决定调用哪个方法
- **工作原理**：
  1. 对象 `o` 是类 `C1, C2, ..., Cn-1, Cn` 的实例（继承链）
  2. `Cn` 是最通用的类（通常是 `object`），`C1` 是最具体的类
  3. 当 `o` 调用方法 `p` 时，Python 按顺序在 `C1, C2, ..., Cn` 中搜索方法实现
  4. 找到第一个匹配的方法就调用它

### 示例
```python
def displayObject(obj):  # 参数类型是 GeometricObject
    print(obj)           # 多态：可以传入 Circle 或 Rectangle
    print(f"Area: {obj.getArea()}")

circle = Circle(5.0)
rectangle = Rectangle(4.0, 3.0)

displayObject(circle)     # 调用 Circle 的 __str__ 和 getArea
displayObject(rectangle) # 调用 Rectangle 的 __str__ 和 getArea
```

### isinstance() 函数
- **作用**：判断对象是否是某个类的实例
- **语法**：`isinstance(对象, 类名)`
- **示例**：
```python
circle = Circle(5.0)
print(isinstance(circle, Circle))          # True
print(isinstance(circle, GeometricObject)) # True（继承关系）
print(isinstance(circle, Rectangle))       # False
```

### 使用isinstance实现条件逻辑
```python
def displayObject(obj):
    print(obj)
    print(f"Area: {obj.getArea()}")
    print(f"Perimeter: {obj.getPerimeter()}")
    
    if isinstance(obj, Circle):
        print(f"Diameter: {obj.getRadius() * 2}")
    elif isinstance(obj, Rectangle):
        print(f"Width: {obj.getWidth()}, Height: {obj.getHeight()}")
```

---

## object类及其方法

### object类
- **定义**：Python 中所有类的基类
- **特点**：如果定义类时不指定继承，默认继承自 `object`
- **等价写法**：
```python
class MyClass:              # 隐式继承 object
    pass

class MyClass(object):      # 显式继承 object（推荐）
    pass
```

### object类的重要方法

#### `__str__()` 方法
- **作用**：返回对象的字符串描述
- **调用时机**：使用 `print()` 或 `str()` 时
- **建议**：应该在自定义类中重写此方法，返回有用的描述

```python
class Circle:
    def __str__(self):
        return f"Circle(radius={self.__radius})"

circle = Circle(5.0)
print(circle)  # 输出：Circle(radius=5.0)
```

#### `__eq__()` 方法
- **作用**：判断两个对象是否相等
- **默认行为**：比较对象的 id（身份），即 `is` 操作
- **重写**：可以自定义相等性判断逻辑

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True（如果重写了__eq__）
```

#### `__new__()` 方法
- **作用**：创建新对象（在 `__init__()` 之前调用）
- **通常**：不需要重写，只在特殊情况下使用
- **工作流程**：
  1. `__new__()` 创建对象
  2. `__init__()` 初始化对象

### 正确的Python风格
- **`__new__()`**：负责创建新对象
- **`__init__()`**：负责初始化对象（通常只需要重写这个）

---

## 多继承

### 定义
- **多继承（Multiple Inheritance）**：一个类可以从多个父类继承属性和方法
- **语法**：`class 子类(父类1, 父类2, ...):`

### 示例
```python
class A:
    def method_a(self):
        print("Method from A")

class B:
    def method_b(self):
        print("Method from B")

class C(A, B):  # 多继承：C 继承 A 和 B
    def method_c(self):
        print("Method from C")

obj = C()
obj.method_a()  # 来自 A
obj.method_b()  # 来自 B
obj.method_c()  # 来自 C
```

### 方法解析顺序（MRO）
- **定义**：Python 按照特定顺序搜索方法（Method Resolution Order）
- **规则**：从左到右，深度优先
- **查看MRO**：`类名.__mro__` 或 `类名.mro()`

### 示例：复杂的多继承
```python
class Animal:
    def eat(self):
        print("Eating")

class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Animal, Flyable, Swimmable):
    def quack(self):
        print("Quack")

duck = Duck()
duck.eat()    # 来自 Animal
duck.fly()    # 来自 Flyable
duck.swim()   # 来自 Swimmable
duck.quack()  # 来自 Duck
```

### 注意事项
- 多继承可能导致方法名冲突
- Python 使用 MRO 解决冲突
- 建议谨慎使用多继承，优先考虑组合（composition）

---

## 常见易错点

1. **忘记self参数**：
   ```python
   def getArea(self):  # 正确
       return self.radius * self.radius
   
   def getArea():      # 错误！缺少self
       return radius * radius
   ```

2. **在类外部访问私有字段**：
   ```python
   circle = Circle(5.0)
   print(circle.__radius)  # 错误！AttributeError
   ```

3. **忘记调用super().__init__()**：
   ```python
   class Circle(GeometricObject):
       def __init__(self, radius):
           super().__init__()  # 必须调用父类构造函数
           self.__radius = radius
   ```

4. **混淆类变量和实例变量**：
   ```python
   class Circle:
       pi = 3.14159          # 类变量（所有实例共享）
       
       def __init__(self, radius):
           self.radius = radius  # 实例变量（每个实例独立）
   ```

5. **直接修改私有字段**：
   ```python
   # 应该使用 getter/setter 方法
   circle.setRadius(10.0)    # 正确
   circle.__radius = 10.0    # 错误！违反了封装原则
   ```

---

## 实践示例

### 示例1：Rectangle类
```python
class Rectangle:
    def __init__(self, width=1.0, height=2.0):
        self.__width = width
        self.__height = height
    
    def getArea(self):
        return self.__width * self.__height
    
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def setWidth(self, width):
        if width > 0:
            self.__width = width
    
    def setHeight(self, height):
        if height > 0:
            self.__height = height
```

### 示例2：Student类
```python
class Student:
    def __init__(self, name, age, grade, student_id, major):
        self.__name = name
        self.__age = age
        self.__grade = grade
        self.__student_id = student_id
        self.__major = major
    
    def isPassed(self):
        return self.__grade >= 60
    
    def updateGrade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
    
    def getPerformance(self):
        if self.__grade >= 90:
            return "Excellent"
        elif self.__grade >= 80:
            return "Good"
        elif self.__grade >= 70:
            return "Average"
        else:
            return "Poor"
    
    def displayInfo(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Grade: {self.__grade}")
        print(f"ID: {self.__student_id}")
        print(f"Major: {self.__major}")
        print(f"Performance: {self.getPerformance()}")
```

---

## 总结

面向对象编程的核心概念：
- **封装**：将数据和方法组合在一起，隐藏实现细节
- **继承**：代码复用，建立 is-a 关系
- **多态**：同一接口处理不同类型，提高代码灵活性
- **抽象**：分离实现和使用，提高代码可维护性

掌握这些概念后，可以设计出结构清晰、易于维护和扩展的Python程序。

