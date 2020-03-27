### 1 ### 1st feature is to identify the optimal amount of calories for the person ###
age = int(input("What is your age: "))
gender = input('What is your gender: ')
weight = int(input('What is your weight: '))
height = int(input('What is your height: '))

if gender == 'male':
  c1 = 66
  h = 6.2 * height
  w= 12.7 * weight
  am = 6.76 * age
  bmr_result = c1 + h + w - am
elif gender == 'female':
  c1 = 655.1
  h = 4.35 * height
  w = 4.7 * weight
  am = 4.7 * age
  bmr_result = c1 + h + w - am
print(bmr_result)

### 2 ### Second feature is to calculate the calories the user get.

import json
with open("food_data.json") as food_data:
  print(food_data)
  json_data = json.load(food_data)

while (True):
  food_name = input("Please insert a food name:")

  food_calories = 0
  for food in json_data["foods"]:
    if(food["food_name"] == food_name):
      food_calories = food["calories"]
      break

  if food_calories > 0:
    grams = float(input("Please insert a grams of the specific food that you eat:"))
    new_calories = grams*food_calories
    print(new_calories)
    break
  else:
    print("There is no data about the food that you eat, please insert other food you had today.")


### 3 ####3rd feature is to calculate the difference between the optimal amount of calories and the calories that the user has alredy got.

bmr_result = int(input("Please insert yout bmr:"))
new_calories = int(input("Please insert calories that you get:"))
if (bmr_result - new_calories > 0):
  diff = bmr_result - new_calories
  print("Remains to eat" ,diff, "calories")
else:
  print("Stop eating :D ")
