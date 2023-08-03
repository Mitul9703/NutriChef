# NutriChef


The Meal Planner Web Application is an advanced tool that empowers users to create personalized meal plans based on their individual needs and dietary preferences. The application considers various factors such as weight, target weight, age, height, and dietary choices like keto and vegetarian to provide tailored meal recommendations. It uses a sophisticated Knapsack problem solved through the Branch and Bound algorithm to optimize the daily calorie, protein, fat, and carbohydrate distribution for users.

## Features

- **User Authentication:** The application includes a secure login system to ensure that users can access and manage their meal plans securely.

- **Personalized Meal Plans:** Users can input their weight, target weight, age, height, and dietary preferences. The application then generates personalized meal plans based on the provided information.

- **Health and Nutrition Tracking:** The application calculates and displays daily calorie, protein, fat, and carbohydrate intake, helping users track their nutrition to meet their health goals.

- **Recipe Recommendations:** The meal plans include recipe recommendations, considering users' dietary choices like keto and vegetarian, to provide a variety of options for each meal.

- **Knapsack Problem Optimization:** The application uses the Branch and Bound algorithm to optimize the meal plans, ensuring that the selected recipes meet users' nutritional requirements while satisfying their dietary preferences.

## How It Works

1. **Login or Sign Up:** Users can either log in to their existing accounts or sign up to access the meal planner features.

2. **Input User Information:** Upon logging in, users can input their weight, target weight, age, height, and select dietary preferences such as keto or vegetarian.

3. **Generate Meal Plan:** Based on the provided information, the application generates a personalized meal plan with recipes that align with the user's health goals and dietary choices.

4. **View Nutrition Information:** Users can view the total daily calorie, protein, fat, and carbohydrate intake of their meal plans, ensuring they stay on track with their nutritional needs.

5. **Recipe Recommendations:** The application provides a list of recipe recommendations for each meal, ensuring a diverse and enjoyable meal experience for users.

6. **Track Progress:** Users can track their progress and make adjustments to their meal plans as needed.


## Setup and Installation

To run the Meal Planner Web Application locally, follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Set up Firebase credentials for authentication and Firestore database.

4. Run the application using `python app.py`.

5. Access the application on your local server (e.g., http://localhost:5000).

## Conclusion

The Meal Planner Web Application is a powerful tool for users to achieve their health and dietary goals. With personalized meal plans, nutritional tracking, and recipe recommendations, users can maintain a healthy lifestyle effortlessly. The optimization algorithms ensure that the meal plans are both nutritious and delicious, making the journey to better health an enjoyable one.
