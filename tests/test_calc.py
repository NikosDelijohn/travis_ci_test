from travis_ci_test.calc import Calculator

def test_add():
    x,y = 1 , 2
    obj = Calculator(x,y)

    assert x+y == obj.add() , "Add Error"

def test_sub():
    x,y = 3 , 1

    obj = Calculator(x, y)

    assert x - y == obj.sub(), "Sub Error"

def test_mul():
    x,y = 3 , 1

    obj = Calculator(x, y)

    assert x * y == obj.mul(), "Mul Error"

def test_div():
    x,y = 3 , 1

    obj = Calculator(x, y)

    assert x / y == obj.div(), "DivError"
