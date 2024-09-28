my_foods=['githeri','pilau','lettuce','mukimo']
myfrens_food=my_foods[:]
my_foods.append('Choma')
myfrens_food.append('ugali')

print("\nmy friend's favourite foods are:")
for foods in my_foods:
    print(foods)
print("My favourite foods are:")
for foods in myfrens_food:
    print(foods)

#exercise
crops=['maize','beans','peas','avocado']
myfrens_crops=crops[:]
crops.append('wheat')
myfrens_crops.append('orange')

print("\nMy crops are:")
for crop in crops:
    print(crop)

print("\n My friend's crops are:")
for crop in myfrens_crops:
   print(crop)