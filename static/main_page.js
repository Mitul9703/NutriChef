document.addEventListener('DOMContentLoaded', function() {
    
  const weightIncreaseBtn = document.getElementById('weight-increase');
  const weightDecreaseBtn = document.getElementById('weight-decrease');

  if (weightIncreaseBtn && weightDecreaseBtn) {
    

    weightIncreaseBtn.addEventListener('click', function () {
      weightamount++;
      console.log(weightamount);
      updateWeight(weightamount);
    });

    weightDecreaseBtn.addEventListener('click', function () {
      if (weightamount > 0) {
        weightamount--;
        console.log(weightamount);
        updateWeight(weightamount);
      }
    });
  } else {
    console.log('Error: Could not find weight buttons.');
  }
    
  
  
    const mealPlanButton = document.getElementById('meal-plan-button');
    mealPlanButton.addEventListener('click', function() {
      // Add your code for the "View Meal Plan" button click event here
      console.log('View Meal Plan button clicked');
    });
  });
  
  function updateWeight(amount) {
    const weightCount = document.getElementById('current-weight');
    weightCount.innerHTML = `${amount}`;
  }

  

  async function fetchdata() {
    try {
      const response = await fetch("/user_data.json");
      const data = await response.json();
      const userData = {
        calories: data.Calories,
        protein: data.Protein,
        carbs: data.Carbs,
        fat: data.Fat,
        weight: data.weight,
        height: data.height,
        age: data.age,
        gender: data.gender,
        targetWeight: data["Targetweight"],
        activity : data["activity"],
        vegetarian : data.vegetarian

      };

      const currentWeightElement = document.getElementById("current-weight");
      const targetWeightElement = document.getElementById("target-weight");
      
      currentWeightElement.textContent = String(userData.weight);
      targetWeightElement.textContent = String(userData.targetWeight);
      weightamount = userData.weight
      updateWeight(userData.weight)

      // Update the HTML content with the height and activity values
      const heightElement = document.getElementById('height-count');
      const activityElement = document.getElementById('activity-text');
      const calElement = document.getElementById('Calorie-count');
      const protElement = document.getElementById('Protein-text');
      const carbElement = document.getElementById('Carbs-text');
      const fatElement = document.getElementById('Fat-text');
      const ageElement = document.getElementById('age-text');
      const vegElement = document.getElementById('veg-text');

      heightElement.textContent = String(userData.height);
      activityElement.textContent = userData.activity;
      calElement.textContent = String(userData.calories);
      protElement.textContent = String(userData.protein);
      carbElement.textContent = String(userData.carbs);
      fatElement.textContent = String(userData.fat);
      ageElement.textContent = String(userData.age);
      vegElement.innerHTML = userData.vegetarian ? `<span style="color:#00b81c">Vegetarian</span>` : `<span style="color:red">Non-vegetarian</span>`

      return userData;
    } catch (error) {
      console.log('Error fetching user data:', error);
      return {};
    }
  }

  fetchdata();

  // Get the height and activity values from the fetched data
const height = 175;
const activity = 'moderately active';

// Update the HTML content with the height and activity values
const heightElement = document.getElementById('height-count');
const activityElement = document.getElementById('activity-text');

heightElement.textContent = height;
activityElement.textContent = activity;
