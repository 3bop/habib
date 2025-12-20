# -------------------------------------- The Start ----------------------------------------------------------------------
#----------------------------
#-- Set --
#-----------
#[1] Set items are enclosed in curly braces {}
#[2] set items are not ordered and not indexed
#[3] set indexing and slicing cant be done
#[4] set has only immutable data types (numbers, strings, tuples) list and dict are not
#[5] set items is unique 
# ---------------------------

# Not ordered and not indexed # غير مرتبة و غير مفهرسة

mySetOne = {"Habib", "Eldabea", 100}
print(mySetOne) # whole set بطباعة المجموعه كامله بدون ترتيب او فهرسه

# print(mySetOne[1]) # TypeError: 'set' object is not subscriptable # لا يمكن الوصول الى عناصر المجموعه عن طريق الفهرسه

# mytuple = (1, 2, 3, 4, 5)
# print(mytuple[0:3]) # (1, 2, 3) # يمكن الوصول الى عناصر التاببل عن طريق الفهرسه
mySetTwo = {1, 2, 3, 4, 5} 
# print(mySetTwo[0:3]) # TypeError: 'set' object is not subscriptable # لا يمكن الوصول الى عناصر المجموعه عن طريق الفهرسه

# has only immutable data types # يحتوي فقط على انواع بيانات غير قابله للتغيير
# mySetThree = {1, "Habib", True, [1, 2, 3]} # TypeError: unhashable type: 'list' # لا يمكن اضافه الليست الى المجموعه
# print(mySetThree) # لا يمكن اضافه الليست الى المجموعه
mySetFour = {1, "Habib", True, (1, 2, 3)} # يمكن اضافه التاببل الى المجموعه
print(mySetFour) # {1, (1, 2, 3), 'Habib'} # التاببل تمت اضافته الى المجموعه

# set items is unique # عناصر المجموعه فريده
mySetFive = {1, 2, "Habib", "one", 1, 2, "Habib"}
print(mySetFive) 
