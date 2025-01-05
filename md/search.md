Python 的 **LEGB（Local -> Enclosing -> Global -> Built-in）**  规则决定了变量的查找顺序和作用域。下面是对每一层作用域的详细说明以及它们的查找规则和示例。

---

1. **Local（本地作用域）** **定义** ：
- 函数或代码块内定义的变量，称为本地变量，仅在函数内部有效。

- 函数内部查找变量时，首先会从本地作用域开始查找。
**特性** ：
- 只在函数内部生效，函数调用结束后变量会被销毁。

- 如果和全局变量重名，本地变量优先。
**示例** ：

```python
def local_scope():
    local_var = "I am local"  # 本地变量
    print(local_var)  # 只能在函数内部访问

local_scope()
# print(local_var)  # 报错：NameError: name 'local_var' is not defined
```


---

2. **Enclosing（嵌套作用域）** **定义** ：
- 嵌套函数的外层函数作用域。

- 如果本地作用域中找不到变量，Python 会查找是否在外层函数的作用域中定义（适用于嵌套函数）。
**特性** ： 
- 嵌套函数可以访问外层函数的变量，但不能直接修改（除非使用 `nonlocal` 关键字）。

- 如果嵌套函数中定义了一个同名变量，会遮蔽外层变量。
**示例** ：

```python
def outer_function():
    outer_var = "I am in enclosing scope"

    def inner_function():
        print(outer_var)  # 可以访问外层函数变量

    inner_function()

outer_function()
```
**Python 的 **LEGB（Local -> Enclosing -> Global -> Built-in）**  规则决定了变量的查找顺序和作用域。下面是对每一层作用域的详细说明以及它们的查找规则和示例。

---

1. **Local（本地作用域）** **定义** ：
- 函数或代码块内定义的变量，称为本地变量，仅在函数内部有效。

- 函数内部查找变量时，首先会从本地作用域开始查找。
**特性** ：
- 只在函数内部生效，函数调用结束后变量会被销毁。

- 如果和全局变量重名，本地变量优先。
**示例** ：

```python
def local_scope():
    local_var = "I am local"  # 本地变量
    print(local_var)  # 只能在函数内部访问

local_scope()
# print(local_var)  # 报错：NameError: name 'local_var' is not defined
```


---

2. **Enclosing（嵌套作用域）** **定义** ：
- 嵌套函数的外层函数作用域。

- 如果本地作用域中找不到变量，Python 会查找是否在外层函数的作用域中定义（适用于嵌套函数）。
**特性** ： 
- 嵌套函数可以访问外层函数的变量，但不能直接修改（除非使用 `nonlocal` 关键字）。

- 如果嵌套函数中定义了一个同名变量，会遮蔽外层变量。
**示例** ：

```python
def outer_function():
    outer_var = "I am in enclosing scope"

    def inner_function():
        print(outer_var)  # 可以访问外层函数变量

    inner_function()

outer_function()
```
使用 `nonlocal` 修改外层函数变量** ：

```python
def outer_function():
    outer_var = "Original value"

    def inner_function():
        nonlocal outer_var  # 声明为外层变量
        outer_var = "Modified value"

    inner_function()
    print(outer_var)  # 输出：Modified value

outer_function()
```


---

3. **Global（全局作用域）** **定义** ：
- 全局变量是定义在函数之外的变量，可在模块内的任何地方访问。

- 如果在本地作用域和嵌套作用域中都找不到变量，Python 会在全局作用域中查找。
**特性** ： 
- 函数内部若想修改全局变量，需使用 `global` 声明。

- 全局变量生命周期与脚本运行时间一致。
**示例** ：

```python
global_var = "I am global"

def global_scope():
    print(global_var)  # 可以在函数内部访问全局变量

global_scope()

# 修改全局变量
def modify_global():
    global global_var
    global_var = "Modified global"

modify_global()
print(global_var)  # 输出：Modified global
```


---

4. **Built-in（内置作用域）** **定义** ： 
- 内置作用域包含 Python 解释器预定义的保留名称，比如 `len`、`print`、`int` 等。

- 如果在本地、嵌套和全局作用域中都找不到变量，Python 会查找内置作用域。
**示例** ：

```python
# 内置函数 len
print(len([1, 2, 3]))  # 输出：3

# 覆盖内置函数（不推荐）
len = "shadowing built-in"
print(len)  # 输出：shadowing built-in
# 如果此时使用 len([1, 2, 3]) 会报错
```


---


### 查找顺序（LEGB）总结 

Python 会按照如下顺序查找变量，直到找到为止：
 
1. **Local（本地作用域）** ：先查找函数内部。
 
2. **Enclosing（嵌套作用域）** ：如果嵌套了函数，查找外层函数的变量。
 
3. **Global（全局作用域）** ：查找当前模块的全局变量。
 
4. **Built-in（内置作用域）** ：最后查找 Python 内置作用域。
如果所有作用域中都找不到变量，Python 会抛出 `NameError`。

---


### 示例：LEGB 查找顺序 


```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # 输出：local

    inner()
    print(x)  # 输出：enclosing

outer()
print(x)  # 输出：global
```
