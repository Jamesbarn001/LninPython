names=['Joshua','Rose','Faith','joseph']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])
message=f"I love you {names[0].title()}"
print(message)
print(message)
#a messsage to an element in a list
motorcycles=['ducati','honda','tiger','boxer']
print(motorcycles[-1])
message=f"My favourite motorcycle is {motorcycles[0].upper()}"
print(message)
#modifying elemnts
motorcycles[0]="kiyosaki"
print(motorcycles)

#adding - appending 
cars=[]
cars.append('toyota')
cars.append('suzuki')
cars.append('mazda')
cars.append('lamborghini')
print(cars)

#insert
cars.insert(0,'lambo')
print(cars)
cars.insert(5,'rangerover')
cars.insert(6,'urus')
print(cars)

#Assignment
dinner=['Joshua','Bilhah','Faith']
print(f"Hello,{dinner[0].title()} i would like to invite for dinner on friday ")

print(f"Hello,{dinner[1].title()} i would like to invite you for dinner on friday")

print(f"Hello,{dinner[2].title()} i would like to invite you for dinner on friday")

print("Faith will not be able to make it for the dinner")
del dinner[2]
dinner.insert(2,'shawn')
dinner.insert(3,'Alex')
print(f"Hello,{dinner[0].title()} i would like to invite for dinner on friday ")

print(f"Hello,{dinner[1].title()} i would like to invite you for dinner on friday")

print(f"Hello,{dinner[2].title()} i would like to invite you for dinner on friday")
print(f"Hello,{dinner[3].upper()} i would like to invite you for the dinner.")
print("Good news i found  a  larger table for 6")
print(len(dinner))
dinner.insert(0,'Rose')
dinner.insert(2,'theo')
dinner.insert(5,'Mary')
dinner.append('Kate')
print(dinner)
print(f"Hello,{dinner[0].title()} i would like to invite for dinner on friday\n ")

print(f"Hello,{dinner[1].title()} i would like to invite you for dinner on friday\n")

print(f"Hello,{dinner[2].title()} i would like to invite you for dinner on friday\n")
print(f"Hello,{dinner[3].title()} i would like to invite for dinner on friday \n")

print(f"Hello,{dinner[4].title()} i would like to invite you for dinner on friday\n")

print(f"Hello,{dinner[5].title()} i would like to invite you for dinner on friday\n")
print(len(dinner))

print("Iam so sorry but the table wont arrive early enough so only two can be accomodated")
pop1=dinner.pop(7)
pop2=dinner.pop(4)
pop3=dinner.pop(3)
pop4=dinner.pop(2)
pop5=dinner.pop(1)
print(f"Hello,{dinner[0].title()} youre still invited for the dinner\n")
print(f"Hello,{dinner[-1].title()} youre still invited for the dinner")
print(len(dinner))
print(dinner)
del dinner[1]
del dinner[-1]
print(dinner)

