from flask import Flask, render_template, url_for, request, jsonify
from backend import *
from bmr import *

app = Flask(__name__)

data_list = []


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/signup")
def sign_up():
    return render_template("signup.html")


@app.route("/main_page")
def main_page():
    global data_list

    print(data_list)

    if data_list:
        gender = data_list[0]["gender"]
        activity = data_list[0]["activity"]
        Weight = int(data_list[1]["Weight"])
        Height = int(data_list[1]["Height"])
        Target_Weight = int(data_list[1]["Target-weight"])
        age = int(data_list[1]["age"])
        vegetarian = data_list[1]["vegetarian"]

        get_cal(
            weight=Weight,
            height=Height,
            activity_level=activity,
            gender=gender,
            target_weight=Target_Weight,
            age=age,
            vegetarian=vegetarian,
        )

        data_list = []
    else :
        with open("./templates/user_data.json") as file:
            existing_data = json.load(file)
            print('ye',existing_data)

        gender = existing_data["gender"]
        activity = existing_data["activity"]
        Weight = int(existing_data["weight"])
        Height = int(existing_data["height"])
        Target_Weight = int(existing_data["Targetweight"])
        age = int(existing_data["age"])
        vegetarian = existing_data["vegetarian"]

        get_cal(
            weight=Weight,
            height=Height,
            activity_level=activity,
            gender=gender,
            target_weight=Target_Weight,
            age=age,
            vegetarian=vegetarian,
        )

    return render_template("main_page.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/faving")
def faving():
    selected_checkboxes = request.args.getlist(
        "checkboxes"
    )  # Print the selected checkboxes
    return render_template("faving.html")


@app.route("/nutrition_count")
def nutrition_count():
    return render_template("nutrition_count.html")


@app.route("/recipe_list")
def recipe_list():
    global data_list

    with open(r"./templates/user_data.json") as file:
        data = json.load(file)

    calorie_limit = data["Calories"]
    protein_limit = data["Protein"]
    carb_limit = data["Carbs"]
    fat_limit = data["Fat"]
    vegetarian = data["vegetarian"]

    print("YE", calorie_limit, protein_limit, carb_limit, fat_limit, vegetarian)

    main_prg(
        calorie_limit=calorie_limit,
        protein_limit=protein_limit,
        carb_limit=carb_limit,
        fat_limit=fat_limit,
        vegetarian=vegetarian,
    )

    return render_template("recipe_list.html")


@app.route("/process_data", methods=["POST"])
def process_data():
    global data_list
    data = request.json.get("data", [])
    data_list.append(data)
    print("ye", data_list)  # Print the selected checkboxes

    return "Added"


@app.route("/selected_recipes.json", methods=["GET"])
def selected_recipes():
    with open(r"./templates/selected_recipes.json") as file:
        data = json.load(file)

    data = json.dumps(data)
    return render_template("selected_recipes.json")


@app.route("/user_data.json", methods=["GET", "POST"])
def user_data():
    if request.method == "GET":
        with open(r"./templates/user_data.json") as file:
            data = json.load(file)

        data = json.dumps(data)
        return render_template("user_data.json")
    elif request.method == "POST":
        data = request.get_json()
        name = data["username"]      
        details = data['details']
        with open("./templates/user_data.json") as file:
            existing_data = json.load(file)

        user_data = {}
        user_data["username"] = name
        for key in details :
            user_data[key] = details[key]
        

        # Write the updated meal data back to added_meal.json
        with open("./templates/user_data.json", "w") as file:
            json.dump(user_data, file)

        return render_template("user_data.json")


@app.route("/added_meal.json", methods=["GET", "POST"])
def added_meal():
    if request.method == "GET":
        with open("./templates/added_meal.json") as file:
            data = json.load(file)
        return render_template("added_meal.json")

    elif request.method == "POST":
        data = request.get_json()
        day = data["day"]
        meal = data["meal"]

        # Load existing meal data from added_meal.json
        with open("./templates/added_meal.json") as file:
            existing_meals = json.load(file)

        # Append the new meal data to the existing data
        existing_meals[day] = meal

        # Write the updated meal data back to added_meal.json
        with open("./templates/added_meal.json", "w") as file:
            json.dump(existing_meals, file)

        return render_template("added_meal.json")


@app.route("/planned_meal")
def planned_meal():
    return render_template("planned_meal.html")


if __name__ == "__main__":
    app.run(debug=True)
