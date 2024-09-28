
#USING IS STATEMENTS WITH LISTS
#Checking for special items
desert=['redvelvet','passion','fruit','blackforest','blueberry']
for cake in desert:
 if cake =='passion':
  print("We dont have this cake at the moment")
 else:
  print (f"Add {cake.title()} to the plate")
print("Your meal is ready to be served.\n")

#Checking if a list is empty
desert=[]

if desert:
 for cake in desert:
  print(f"Add{cake.title() }to the plate ")
else:
 print("Are you sure you want a plain plate?")

 #Using multiple lists
 desert=['redvelvet','passion','fruit','blackforest','blueberry']
 req_desert=['passion','ngumu','watermelon','blackforest']
 for cake in req_desert:
  if cake in desert:
   print(f"Adding {cake.title()} to plate.")
  else:
   print(f"Sorry we can not find {cake.title()}")

 #Assignment
usernames=['admin','juniora','ceeeo','ctooo','technician','engineer']
for name in usernames:
 print(f"Hello {name.title()}, Welcome to this website.Get ready to be productive today\n")
 if name=='admin':
  print(f"Hello {name.title()}, would you like to see a status report?")
 if name=='admin':
  name='jayden'
  print(f"Hello {name.title()}, thank you for logging in again")

#check 
username=[]
if username:
 for names in username:
   print(f"Hello {names.title()}, Welcome to this website.Get ready to be productive today\n")
else:
  print("We need to find some more users.")

#Multiple lists
current_users=['John','Mary','Luke','Joshua','matthew','Rose']
new_users=['James','Rose','King','Luke','Joshua']
current_usersl=[user.lower() for user in current_users]
print(current_users)
print(current_usersl)
for user in new_users:
 if user in current_users and current_usersl:
  print("This username is already taken use another one")
 else:
   print("THE USERNAME IS AVAILABLE")

#ordinal numbers
numbers = ['1','2','3','4','5','6','7','8','9']
print(numbers)
for number in numbers:
 if number =='1':
  print(f"{number}st")
 elif number =='2':
   print(f"{number}nd")
 elif number =='3':
   print(f"{number}rd")
 else:
   print(f"{number}th")