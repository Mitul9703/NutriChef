import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("adsproj-f1323-firebase-adminsdk-2ejx9-7eeee89a2f.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_cal(weight, height, age, gender, activity_level, target_weight, vegetarian, weight_loss_per_month=1):
    def calculate_bmr(weight, height, age, gender):
        if gender == 'male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr

    def calculate_calorie_intake(bmr, activity_level):
        activity_factors = {
            'sedentary': 1.2,
            'lightly active': 1.375,
            'moderately active': 1.55,
            'very active': 1.725,
            'extra active': 1.9
        }
        return bmr * activity_factors[activity_level]

    def calculate_macronutrients(calorie_intake):
        protein_intake = 0.15 * calorie_intake / 4
        carb_intake = 0.55 * calorie_intake / 4
        fat_intake = 0.3 * calorie_intake / 9
        return protein_intake, carb_intake, fat_intake

    bmr = calculate_bmr(weight, height, age, gender)
    calorie_intake = calculate_calorie_intake(bmr, activity_level)

    if target_weight < weight:
        # Calculate the calorie deficit required for weight loss goal
        calorie_deficit = weight_loss_per_month * 7700 / 30  # Assuming 7700 calories for 1 kg of weight loss
        calorie_intake_adjusted = calorie_intake - calorie_deficit
    elif target_weight > weight:
        # Calculate the calorie surplus required for weight gain goal
        calorie_surplus = weight_loss_per_month * 7700 / 30  # Assuming 7700 calories for 1 kg of weight gain
        calorie_intake_adjusted = calorie_intake + calorie_surplus
    else:
        # Maintain weight
        calorie_intake_adjusted = calorie_intake

    protein_intake, carb_intake, fat_intake = calculate_macronutrients(calorie_intake_adjusted)

    print(f"Daily Calorie Intake: {calorie_intake_adjusted} calories")
    print(f"Daily Protein Intake: {protein_intake} grams")
    print(f"Daily Carbohydrate Intake: {carb_intake} grams")
    print(f"Daily Fat Intake: {fat_intake} grams")

    user_data = {
        "Calories": int(calorie_intake_adjusted),
        "Protein": int(protein_intake),
        "Carbs": int(carb_intake),
        "Fat": int(fat_intake),
        "weight": weight,
        "height": height,
        "age": age,
        "gender": gender,
        "Targetweight": target_weight,
        "vegetarian": vegetarian,
        "activity": activity_level
    }

    with open("./templates/user_data.json") as file:
            existing_data = json.load(file)

        # Append the new meal data to the existing data
    for key in user_data :
            existing_data[key] = user_data[key]
    username = existing_data['username']
    
    db.collection("users").document(username).update(existing_data)

        # Write the updated meal data back to added_meal.json
    with open("./templates/user_data.json", "w") as file:
            json.dump(existing_data, file,indent=4)

