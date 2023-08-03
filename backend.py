import json
from collections import deque
import heapq
import random

class Recipe:
    def __init__(self, title, ingredients, health_score, missing_ingredients, vegetarian, gluten_free, ready_in_minutes, price_per_serving, source_url, image_url, summary, servings, instructions, calories, fat, carbohydrates, protein):
        self.title = title
        self.ingredients = ingredients
        self.health_score = health_score
        self.missing_ingredients = missing_ingredients
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free
        self.ready_in_minutes = ready_in_minutes
        self.price_per_serving = price_per_serving
        self.source_url = source_url
        self.image_url = image_url
        self.summary = summary
        self.servings = servings
        self.instructions = instructions
        self.calories = int(calories)
        self.fat = int(fat)
        self.carbohydrates = int(carbohydrates)
        self.protein = int(protein)

class RecipeGraph:
    def __init__(self):
        self.graph = {}

    def add_recipe(self, recipe):
        for ingredient in recipe.ingredients:
            if ingredient not in self.graph:
                self.graph[ingredient] = []
            self.graph[ingredient].append(recipe)

    def get_top_recipes(self, n):
        all_recipes = []

        for ingredient in self.graph:
            all_recipes.extend(self.graph[ingredient])

        random.shuffle(all_recipes)
        top_recipes = all_recipes[:n]

        return top_recipes


def main_prg(calorie_limit = 2000,protein_limit = 80,carb_limit = 120,fat_limit = 100,vegetarian = False) :


    
    with open(r'./static/recipes_maincourse.json') as file:
        data = json.load(file)

    with open(r'./templates/added_meal.json') as file:
        added_meal_data = json.load(file)  
    added_meal_list = []
    for day in added_meal_data :
        for meal in added_meal_data[day] :
            added_meal_list.append(meal['title'])

    with open(r'./templates/selected_recipes.json') as file:
        selected_meal_data = json.load(file)  
    selected_meal_list = []
    for meal in selected_meal_data :
        selected_meal_list.append(meal['title'])
            
      

    

    recipe_graph = RecipeGraph()

    for recipe_data in data:
        if recipe_data['title'] not in added_meal_list and recipe_data['title'] not in selected_meal_list :
            if not vegetarian : 
                recipe = Recipe(recipe_data['title'], recipe_data['ingredients'], recipe_data['healthScore'], [], recipe_data['vegetarian'], recipe_data['glutenFree'], recipe_data['readyInMinutes'], recipe_data['pricePerServing'], recipe_data['sourceUrl'], recipe_data['imageUrl'], recipe_data['summary'], recipe_data['servings'], recipe_data['instructions'], recipe_data['Calories'], recipe_data['Fat'], recipe_data['Carbohydrates'], recipe_data['Protein'])
                recipe_graph.add_recipe(recipe)
            else :
                if recipe_data['vegetarian'] :
                    recipe = Recipe(recipe_data['title'], recipe_data['ingredients'], recipe_data['healthScore'], [], recipe_data['vegetarian'], recipe_data['glutenFree'], recipe_data['readyInMinutes'], recipe_data['pricePerServing'], recipe_data['sourceUrl'], recipe_data['imageUrl'], recipe_data['summary'], recipe_data['servings'], recipe_data['instructions'], recipe_data['Calories'], recipe_data['Fat'], recipe_data['Carbohydrates'], recipe_data['Protein'])
                    recipe_graph.add_recipe(recipe)

    n = 100  
    top_recipes = set(recipe_graph.get_top_recipes(n))


    def knapsack_recipes(recipes, calorie_limit, protein_limit, carb_limit, fat_limit):
        n = len(recipes)
        best_recipes = []
        best_score = float('-inf')
        feasible_solution_found = False

        def calculate_score(recipe):
            return recipe.health_score

        def calculate_calories_diff(calories):
            return abs(calories - calorie_limit)

        def backtrack(index, current_calories, current_protein, current_carbs, current_fat, current_recipes, selected_indices):
            nonlocal best_score, best_recipes, feasible_solution_found

            if len(current_recipes) == 4:
                score = sum(calculate_score(recipe) for recipe in current_recipes)

                if (
                    abs(current_calories - calorie_limit) <= 200
                    and abs(current_protein - protein_limit) <= 20 
                    and abs(current_carbs - carb_limit) <= 20
                    and abs(current_fat - fat_limit) <= 20
                    and score > best_score
                ):
                    best_score = score
                    best_recipes = current_recipes.copy()
                    feasible_solution_found = True

                return

            if index == n:
                return

            recipe = recipes[index]

            if (
                current_calories + recipe.calories <= calorie_limit
                and index not in selected_indices
            ):
                current_recipes.append(recipe)
                selected_indices.append(index)
                backtrack(
                    index + 1,
                    current_calories + recipe.calories,
                    current_protein + recipe.protein,
                    current_carbs + recipe.carbohydrates,
                    current_fat + recipe.fat,
                    current_recipes,
                    selected_indices
                )
                current_recipes.pop()
                selected_indices.pop()

            if not feasible_solution_found:
                backtrack(
                    index + 1,
                    current_calories,
                    current_protein,
                    current_carbs,
                    current_fat,
                    current_recipes,
                    selected_indices
                )

        recipes.sort(key=calculate_score, reverse=True)
        backtrack(0, 0, 0, 0, 0, [], [])

        if not feasible_solution_found:
            print('called')
            recipes_list_titles = []
            recipes_list = []
            for recipe in recipes :
                if recipe.title not in recipes_list_titles :
                    recipes_list_titles.append(recipe.title)
                    recipes_list.append(recipe)
            recipes_list.sort(key=lambda r: abs(r.calories - calorie_limit))
            return recipes_list[:4]

        return best_recipes[:4]




    selected_recipes = knapsack_recipes(
        [recipe for recipe in top_recipes],
        calorie_limit,
        protein_limit,
        carb_limit,
        fat_limit,
        
    )

    total_calories = sum(recipe.calories for recipe in selected_recipes)
    total_protein = sum(recipe.protein for recipe in selected_recipes)
    total_carbs = sum(recipe.carbohydrates for recipe in selected_recipes)
    total_fat = sum(recipe.fat for recipe in selected_recipes)


    print("Total:")
    print(
        f"Calories: {total_calories} | Protein: {total_protein}g | Carbs: {total_carbs}g | Fat: {total_fat}g"
    )

    selected_recipe_data = []

    for recipe in selected_recipes:
        recipe_data = {
            "title": recipe.title,
            "ingredients": recipe.ingredients,
            "health_score": recipe.health_score,
            "missing_ingredients": recipe.missing_ingredients,
            "vegetarian": recipe.vegetarian,
            "gluten_free": recipe.gluten_free,
            "ready_in_minutes": recipe.ready_in_minutes,
            "price_per_serving": recipe.price_per_serving,
            "source_url": recipe.source_url,
            "image_url": recipe.image_url,
            "summary": recipe.summary,
            "servings": recipe.servings,
            "instructions": recipe.instructions,
            "calories": recipe.calories,
            "fat": recipe.fat,
            "carbohydrates": recipe.carbohydrates,
            "protein": recipe.protein
        }
        selected_recipe_data.append(recipe_data)

    with open(r'./templates/selected_recipes.json', 'w') as file:
        json.dump(selected_recipe_data, file, indent=4)


