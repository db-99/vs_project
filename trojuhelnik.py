import math

def delkaStrany(x1, y1, x2, y2):
    """Calculate the length of a side of a triangle.

    Return the length of the side rounded to 2 decimal places
    >>> delkaStrany(10, 10, 5, 5) == 7.07
    True
    >>> delkaStrany(6, 4, 2, 3)
    4.12
    """
    str1 = x2-x1
    str2 = y2-y1
    str1 = math.pow(str1, 2)
    str2 = math.pow(str2, 2)
    st = round(math.sqrt(str1+str2), 2)
    return st

def getObvod(a, b, c):
    """Calculate the perimeter of a triangle.

    Return the perimeter of the triangle
    >>> getObvod(5, 10, 20) == 35
    True
    >>> getObvod(1, 2, 3)
    6
    """
    o = a + b + c
    return o

def getObsah(a, b, c):
    """Calculate the area of a triangle.

    Return the area of the triangle rounded to 2 decimal places
    (if possible to calculate)
    >>> getObsah(6, 4, 5) == 9.92
    True
    >>> getObsah(1, 1, 23) >= 0
    False
    >>> getObsah(5, 5, 5)
    10.83
    >>> getObsah(2, 4, 8)
    -1
    """
    s = (a + b + c) / 2
    m = s * (s - a) * (s - b) * (s - c)
    if m >= 0:
        obs = round(math.sqrt(m), 2)
    else:
        obs = -1
    return obs

def jeSestrojitelny(a, b, c):
    """Calculate if a triangle is valid.

    Return true or false based on the validity of the triangle
    >>> jeSestrojitelny(50, 100, 1)
    False
    >>> jeSestrojitelny(12, 13, 14)
    True
    """
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

def jePravouhly(a, b, c):
    """Calculate if a triangle is a right triangle.

    Return true if the triangle is a right triangle or false if it is not
    >>> jePravouhly(3, 5, 4)
    True
    >>> jePravouhly(4, 3, 5)
    True
    >>> jePravouhly(5, 3, 4)
    True
    >>> jePravouhly(74, 73, 72)
    False
    """
    cond1 = math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2)
    cond2 = math.pow(b, 2) == math.pow(c, 2) + math.pow(a, 2)
    cond3 = math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2)
    if cond1 or cond2 or cond3:
        return True
    else:
        return False

def trojuhelnik():
    """Calculate various properties of a triangle.

    Calculate the length of the sides, the perimeter and
    the area (if possible to calculate) of a triangle based on the entered
    coordinates of its three vertices.
    Also calculate if the triangle is valid and if it is a right triangle.
    """
    print("Zadejte souřadnice pro bod A na ose X: ")
    ax = float(input())
    print("Zadejte souřadnice pro bod A na ose Y: ")
    ay = float(input())
    print("Zadejte souřadnice pro bod B na ose X: ")
    bx = float(input())
    print("Zadejte souřadnice pro bod B na ose Y: ")
    by = float(input())
    print("Zadejte souřadnice pro bod C na ose X: ")
    cx = float(input())
    print("Zadejte souřadnice pro bod C na ose Y: ")
    cy = float(input())
    stra = delkaStrany(cx, cy, bx, by)
    print("Délka strany a: " + str(stra) + " cm")
    strb = delkaStrany(ax, ay, cx, cy)
    print("Délka strany b: " + str(strb) + " cm")
    strc = delkaStrany(bx, by, ax, ay)
    print("Délka strany c: " + str(strc) + " cm")
    if jeSestrojitelny(stra, strb, strc):
        print("Trojúhelník je sestrojitelný")
    else:
        print("Trojúhelník není sestrojitelný")
    obvod = getObvod(stra, strb, strc)
    print("Obvod trojúhelníku je " + str(obvod) + " cm")
    obsah = getObsah(stra, strb, strc)
    if obsah >= 0:
        print("Obsah trojúhelníku je " + str(obsah) + " cm")
    else:
        print("Obsah nelze vypočítat (záporné číslo pod odmocninou)")
    if jePravouhly(stra, strb, strc):
        print("Trojúhelník je pravoúhlý")
    else:
        print("Trojúhelník není pravoúhlý")
        
def test_delkaStrany():
    """Unit test for delkaStrany() function."""
    assert delkaStrany(14, 8, 3, 65) == 58.05
    assert (delkaStrany(47, 65, 3, 12) == 68.88) is True
    
def test_getObvod():
    """Unit test for getObvod() function."""
    assert getObvod(23.45, 32.01, 41.34) == 96.8
    assert (getObvod(1.01, 2.35, 9.87) == 13.23) is True
    
def test_getObsah():
    """Unit test for getObsah() function."""
    assert getObsah(14, 17, 23) == 118.49
    assert (getObsah(8, 15, 34) >= 0) is False
def test_jeSestrojitelny():
    """Unit test for jeSestrojitelny() function."""
    assert jeSestrojitelny(1, 88, 55) is False
    assert jeSestrojitelny(76, 67, 55) is True