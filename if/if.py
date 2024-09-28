#equality
car='alex'
if car=='alex':
 print("true")
else:
 print("false")

#inequality
car='lamborghini'
if car != 'lamborghini':
    print("There's been a mistake") 
else:
    print("It was planned to be so")

#comparisons
age=28
if age<=18:
    print("You can begin the application")
if age>=18:
    print("You can not apply this course")

#multiple conditions
#and
age1=20
age2=22
if age1>=18 and age2<=18:
    print("True")
else:
    print("False")
#or
age1=20
age2=22
if age1>=22 or age2<=18:
    print("Tru")
else:
    print("Fals")

#checking a value in a list
people=['martha','mary','koome','kingsley','aaron']
if 'martha' in people:
    print("True")
if 'cate' in people:
    print("True")
else:
    print("False")
   
#checking for a value not in list
user='kendi'
if user not in people:
    print("User cannot be found")

#Assignment
car = 'subaru'
if car=='subaru':
    print("I predict true")
if car!='sedan':
    print("False")

disciples=['peter','andrew','matthew','john','thomas']
if 'peter' in disciples:
    print("True")
if 'Luke' not in disciples:
    print("FALSE")

key1=23
key2=34
if key1>20 or key2<30:
   print('True')
else:
    print("False")

sizes=['small','large','medium','extralarge','vsmall','xxlarge']
if'xxlarge' in sizes:
    print("TRUEE")
if 'small' in sizes:
    print("TRUEEE")
if 's39' not in sizes:
    print("Not available")