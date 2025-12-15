#----------------------------
#-- Lists --
#-----------
#[1] list items are enclosed in square brackets 
#[2] list are ordered, to use index to access items
#[3] list are mutable = add, delete, idit
#[4] list items is not unique
#[5] list can have different data types
#----------------------------

myAwesomeList = ["one", "two", "one", 1, 100.5, True]
print(myAwesomeList) # whole list
print(myAwesomeList[1]) # two
print(myAwesomeList[-3]) # 1

print(myAwesomeList[1:4]) # ['two', 'one', 1]
print(myAwesomeList[:4]) # ['one', 'two', 'one', 1]
print(myAwesomeList[1:]) # ['two', 'one', 1, 100.5, True]

print(myAwesomeList[::1]) # ['one', 'two', 'one', 1, 100.5, True]
print(myAwesomeList[::2]) # ['one', 'one', 100.5]

print(myAwesomeList)
myAwesomeList[1] = 2
myAwesomeList[-1] = False
myAwesomeList[0:2] =[]
myAwesomeList[0:3] = ["A", "B", "C"]
print(myAwesomeList)

######################################THE END##############################################