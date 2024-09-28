

#end with elif
age=20
if age<8:
  price=0
elif age<15:
  price=15
elif age<65:
  price=20
elif age>=65:
  price=40
print(f"Your admission cost is ${price}")