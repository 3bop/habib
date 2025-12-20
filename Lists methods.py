# ------------------------------- The Start --------------------------------------
# -------------------
# -- Lists methods --
# -------------------

# append() # يضيف عنصر في نهاية القائمة
myfriends = ["Habib", "abader", "gorge"]
myfriends.append("yassa")
myfriends.append("100")
myfriends.append("150.200")
myfriends.append("true")
myfriends.append("myoldfriend")
print(myfriends)  # ['Habib', 'abader', 'gorge', 'yassa']

print(myfriends)
print(myfriends[2]) # gorge
print(myfriends[6]) # true
print(myfriends[7]) # myoldfriend
print(myfriends[7][2]) # o

# extend() # دمج قائمتين في قائمة واحدة

a = [1, 2, 3]
b = ["A", "B", "C"]
c = ["one", "two", "three"]
a.extend(b)
a.extend(c)
print(a)  # [1, 2, 3, 'A', 'B

# remove() # يحذف عنصر معين من القائمة

x = [1, 2, 3, 4, 5, "Habib", True ,"Abader", "Gorge"]
x.remove(3)
x.remove("Habib")
x.remove(True)
print(x)  # [1, 2, 4, 5, 'Abader', 'Gorge']

# sort()    ((strings ' numbers)نوع عنصر واحد)ترتيب العناصر تصاعديا

y = [1, 2 , 100, 120, -10, 17, 29]
y.sort()
# y.sort(reverse=True)  # ترتيب تنازليا
print(y) # [-10, 1, 2, 17, 29, 100, 120] 

# reverse()   عكس ترتيب العناصر

z =[10, 1, 9, 80, 100, "Habib", 100]
z.reverse()
print(z)  # [100, 'Habib', 100, 80, 9, 1, 10]
#------------------------------- The End ----------------------------------------