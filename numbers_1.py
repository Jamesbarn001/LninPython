
#exercise

for value in range(0,10):
 print(value)
numbers=list(range(10,22))
print(numbers)
numbers=list(range(9,20))
print(numbers)

squares=[]
for value in range(1,10):
 squares.append(value**2)
print(squares)

cube=[]
for value in range(1,23):
 cube.append(value**3)
print(cube)

for value in range (1,7):
 print(value)
 
numbers=list(range(7)) 
print(numbers)

evennumbers=list(range(2,20,2))
print(evennumbers)

#squares
squares=[]
for value in range(1,12):
  squares.append(value**2)
  print(squares)
 #simple statistics
numbers=[1,2,3,4,5,6,7,8,9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))    

#exercise

#odd numbers
oddnumbers=list(range(0,20,3))
for value in oddnumbers:
 print(value)

 #multiples
multiples=[]
for value in range(3,30):
 multiples.append(value*3)
print(multiples)

#cube
cube=[]
for value in range(10):
 cubes=(value**3)
 cube=cubes
 print(cube)

 #list comprehension
 cubes=[value**3 for value in range(10)]
print(cubes)
 
squares=[value**2 for value in range (15)]
print(squares)