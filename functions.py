
def askUserToInsertAge():
    age = int(input("What is your age: "))
    return age
def askUserToInsertGender():
    gender = input('What is your gender: ')
    return gender
def askUserToInsertWeight():
    weight = int(input('What is your weight: '))
    return weight
def asukUserToInserHeight():
    height = int(input('What is your height: '))
    return height
def calculateBmr(age,gender,weight,height):
    c1=0
    h=0
    w=0
    am=0
    bmr_result=0
    if gender == 'male':
        c1 = 66
        h = 6.2 * height
        w = 12.7 * weight
        am = 6.76 * age
        bmr_result = c1 + h + w - am
    elif gender == 'female':
        c1 = 655.1
        h = 4.35 * height
        w = 4.7 * weight
        am = 4.7 * age
        bmr_result = c1 + h + w - am
    return bmr_result
def printBmr(bmr_result):
    print("Your daily optimal amount of calories is ",bmr_result,"calories")

import json


def getFoodInformation():
    foods = {}
    with open("food_data.json") as food_data:
        foods = json.load(food_data)

    return foods["foods"]


def askUserToInsertFoodName():
    food_name = input("Please insert a food name:")

    return food_name

def checkIfFoodNameIsInJson(food_name,foods):
    food_calories =0
    for food in foods:
        if (food["food_name"]) == food_name:
            food_calories = food["calories"]
            break
    return food_calories



def checkFoodcalories(food_calories):
    new_calories=0
    if food_calories > 0:
        grams = float(input("Please insert a grams of the specific food that you eat(for example if you eat 250 grams please insert 0.25):"))
        new_calories = grams * food_calories

    else:
        print("There is no data about the food that you eat, please insert other food you had today.")

    return new_calories
def printCalories(new_calories):
    print("You have already got",new_calories,"calories")
def calculateRemainingCalories(new_calories,bmr_result):
    if (bmr_result - new_calories > 0):
        diff = bmr_result - new_calories
        print("Remains to eat", diff, "calories")
    else:
        diff = abs(bmr_result - new_calories)
        print("You should stop eating, because you have already got ", diff, "extra calories")

import json

def getExerciseInformation():
    exercises = {}
    with open("exercises_data.json") as exercises_data:
        exercises = json.load(exercises_data)

    return exercises["exercises"]


def askUserToInsertExerciseName():
    exercise_name = input("Please insert a exercise name:")

    return exercise_name

def checkIfExerciseNameIsInJson(exercise_name,exercises):
    burnt_calories =0
    for exercise in exercises:
        if (exercise["exercise_name"]) == exercise_name:
            burnt_calories = exercise["burntCalories"]
            break
    return burnt_calories



def checkExercisecalories(burnt_calories):
    all_burnt_calories=0
    if burnt_calories > 0:
        exerciseAmount = float(input("Please insert how many times have you done this exercise:"))
        all_burnt_calories = exerciseAmount * burnt_calories

    else:
        print("There is no data about the exercise you did")
    return all_burnt_calories
def printBurntCalories(all_burnt_calories):
    print("You have already burnt",all_burnt_calories,"calories")
def main():
    print("Welcome to our App")
    age = askUserToInsertAge()
    gender= askUserToInsertGender()
    weight=askUserToInsertWeight()
    height = asukUserToInserHeight()
    bmr_result=calculateBmr(age,gender,weight,height)
    printBmr(bmr_result)
    foods = getFoodInformation()
    food_name = askUserToInsertFoodName()
    food_calories = checkIfFoodNameIsInJson(food_name,foods)
    new_calories = checkFoodcalories(food_calories)
    printCalories(new_calories)
    calculateRemainingCalories(new_calories, bmr_result)
    exercises = getExerciseInformation()
    exercise_name = askUserToInsertExerciseName()
    burnt_calories = checkIfExerciseNameIsInJson(exercise_name,exercises)
    all_burnt_calories = checkExercisecalories(burnt_calories)
    printBurntCalories(all_burnt_calories)
    print("Thanks for using the App, See you next time")

main()