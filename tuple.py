# ------------------------------- The Start --------------------------------------
#----------------------------
#-- Tuple --
#-----------
#[1] Tuples items are enclosed in parentheses 
#[2] you can remove parentheses if you want 
#[3] tuple are ordered, to use index to access items
#[4] tuple are immutable = you cannot add, delete
#[5] tuple items is not unique
#[6] tuple can have different data types
#[7] operators used in strings and lists available in tuples
#----------------------------

# tuple syntax & type test # تركيب التابل و اختبار النوع

myAwesomeTupleOne = ("Habib", "Eldabea")
myAwesomeTupleTwo = "Habib", "Eldabea"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# tuple indexing # الوصول الى عناصر التابل

myAwesomeTupleThree = (10, 20, 30, 40, 50, 60, 70, 80)
print(myAwesomeTupleThree) # whole tuple # طباعة كل العناصر
print(myAwesomeTupleThree[2]) # 30 #اللوصول الى عنصر معين
print(myAwesomeTupleThree[-3]) # 60  # الوصول الى عنصر معين من النهاية

# tuple Assign values # تعيين قيم لعناصر التابل

myAwesomeTupleFour = ("1", "2", "3", "4", "5")
# myAwesomeTupleFour[2] = "100" # محاولة تعديل عنصر في التابل
# print(myAwesomeTupleFour) # TypeError: 'tuple' object does not support item assignment # لا يمكن تعديل عناصر التابل

# tuple items # الوصول الى عناصر التابل

myAwesomeTupleFive = ("Habib", "Eldabea", "Habib", 100, 200.5, True)
print(myAwesomeTupleFive) # whole tuple
print(myAwesomeTupleFive[1]) # Eldabea
print(myAwesomeTupleFive[1:4]) # ('Eldabea', 'Habib', 100)
print(myAwesomeTupleFive[:4]) # ('Habib', 'Eldabea', 'Habib', 100)
print(myAwesomeTupleFive[1:]) # ('Eldabea', 'Habib', 100, 200.5, True)
print(myAwesomeTupleFive[::1]) # ('Habib', 'Eldabea', 'Habib', 100, 200.5, True)
print(myAwesomeTupleFive[::2]) # ('Habib', 'Habib', 200.5)

# tuple with one element # # تابلي مع عنصر واحد

myTuble = ("Habib")
myTubleTwo = "Habib"

myTubleTree = ("Habib",)
myTubleFure = "Habib",

print(myTuble) # Habib
print(myTubleTwo) # Habib

print(type(myTuble)) # str
print(type(myTubleTwo)) # str
print(type(myTubleTree)) # tuple
print(type(myTubleFure)) # tuple
print(len(myTubleTree)) # 1 # تحديد طول التابل
print(len(myTubleFure)) # 1 # تحديد طول التابل

# Tuble Concatenation # # دمج تابليين

a = (1, 2, 3) 
b = ("A", "B", "C") 
c = a + b # دمج تابليين
print(c)  # (1, 2, 3, 'A', 'B', 'C') # طباعة التابل بعد الدمج

# Tuble, List, String repet (*) # لتكرار التابل و الليست و الستيرنغ

mystring = "Habib"
mylist = [1, 2, 3]
mytuble = ("A", "B", "C")
print(mystring * 3) # HabibHabibHabib
print(mylist * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(mytuble * 3) # ('A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C')

# Methods = count() # يحسب عدد مرات تكرار عنصر معين في التابل 

a = (1, 2, 3, 1, 4, 5, 1, 1, 6, 1)
print(a.count(1))  # 5 # يعد عدد مرات تكرار العنصر 1 في التابل

# Methods = index() # يعيد موقع اول عنصر معين في التابل

b = ("A", "B", "C", "D", "E", "C", "F")
# print("The position of first C is:" + b.index("C")) # error concatenating str and int
print("The position of first C is: {}".format(b.index("C"))) # يعيد موقع اول عنصر C في التابل
print(b.index("C"))  # 2 # يعيد موقع اول عنصر C في التابل
print(b.index("E"))  # 4 # يعيد موقع اول عنصر E في التابل

# Tuple Destruct تفكيك التابل الى متغيرات

a = ("A", "B", "C")
x, y, z = a  # تفكيك التابل الى متغيرات
print(x)  # A
print(y)  # B
print(z)  # C

#a = ("A", "B", 100, "C")
#x, y, z = a  # تفكيك التابل الى متغيرات
#print(x)  # ValueError: too many values to unpack (expected 3)

a = ("A", "B", 100, "C")
x, y, _, z = a  # تفكيك التابل الى متغيرات
print(x)  # A
print(y)  # B
print(z)  # C
# ------------------------------- The End ----------------------------------------