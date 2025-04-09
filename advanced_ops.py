import math

def square(x):
    """計算平方 x²"""
    return x ** 2

def sqrt(x):
    """計算平方根 √x"""
    try:
        return math.sqrt(x)
    except ValueError:
        return "Error"

def reciprocal(x):
    """計算倒數 1/x"""
    try:
        return 1 / x
    except ZeroDivisionError:
        return "Error"

def power(x, y):
    """計算 x 的 y 次方 xʸ"""
    return x ** y

def log10(x):
    """計算常用對數 log10(x)"""
    try:
        return math.log10(x)
    except ValueError:
        return "Error"

def ln(x):
    """計算自然對數 ln(x)"""
    try:
        return math.log(x)
    except ValueError:
        return "Error"