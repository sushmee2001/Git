#Write a Python script to merge two Python dictionaries
a1 = {'a':100,'b':200}
a2 = {'x':300,'y':400}
a = a1.copy()
a.update(a2)
print(a)
