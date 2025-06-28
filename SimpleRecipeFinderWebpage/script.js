const Agnirva_searchButton = document.getElementById('Agnirva_search-button');
const Agnirva_ingredientInput = document.getElementById('Agnirva_ingredient-input');
const Agnirva_recipesDiv = document.getElementById('Agnirva_recipes');

Agnirva_searchButton.addEventListener('click', () => {
  const Agnirva_ingredient = Agnirva_ingredientInput.value.trim();
  if (Agnirva_ingredient === '') {
    alert('Please enter an ingredient.');
    return;
  }
  fetchRecipes(Agnirva_ingredient);
});

async function fetchRecipes(Agnirva_ingredient) {
  Agnirva_recipesDiv.innerHTML = '<p>Loading recipes...</p>';
  try {
    const Agnirva_response = await fetch(`https://www.themealdb.com/api/json/v1/1/filter.php?i=${Agnirva_ingredient}`);
    const Agnirva_data = await Agnirva_response.json();
    displayRecipes(Agnirva_data.meals);
  } catch (Agnirva_error) {
    console.error('Error fetching recipes:', Agnirva_error);
    Agnirva_recipesDiv.innerHTML = '<p>Sorry, something went wrong. Please try again later.</p>';
  }
}

function displayRecipes(Agnirva_meals) {
  if (!Agnirva_meals) {
    Agnirva_recipesDiv.innerHTML = '<p>No recipes found. Try a different ingredient.</p>';
    return;
  }
  Agnirva_recipesDiv.innerHTML = '';
  Agnirva_meals.forEach(Agnirva_meal => {
    const Agnirva_recipeDiv = document.createElement('div');
    Agnirva_recipeDiv.className = 'Agnirva_recipe';

    const Agnirva_mealImg = document.createElement('img');
    Agnirva_mealImg.src = Agnirva_meal.strMealThumb;
    Agnirva_mealImg.alt = Agnirva_meal.strMeal;

    const Agnirva_mealName = document.createElement('div');
    Agnirva_mealName.className = 'Agnirva_recipe-name';
    Agnirva_mealName.textContent = Agnirva_meal.strMeal;

    Agnirva_recipeDiv.appendChild(Agnirva_mealImg);
    Agnirva_recipeDiv.appendChild(Agnirva_mealName);

    Agnirva_recipesDiv.appendChild(Agnirva_recipeDiv);
  });
}

Agnirva_ingredientInput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    Agnirva_searchButton.click();
  }
});
