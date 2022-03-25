"""
lo mismo las tres
"""

myStr = "Ramon"

print("My name is " + myStr)

print((f"My name is {myStr}"))

print("My name in {0}".format(myStr))

x = 2
y = 4

if x > 2 and x <= 10:
    print("x es menor que diez")
if x > 2 or x <= 20:
    print("x es mayor que dos o menor o igual que veinte")
if (not(x == y)):
    print("x no es igual a y")
