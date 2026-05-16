from django.shortcuts import render

recipes = {
    "recipe1": {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"}
        ],
    },
    "recipe2": {
        "name": "Recipe 2",
        "ingredients": [
            {"name": "garlic", "quantity": "1 head"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "vinegar", "quantity": "1/2cup"},
            {"name": "water", "quantity": "1 cup"},
            {"name": "salt", "quantity": "1 tablespoon"},
            {"name": "whole black peppers", "quantity": "1 tablespoon"},
            {"name": "pork", "quantity": "1 kilo"}
        ],
    }
}

def recipe_list(request):
    ctx = {
        "recipes": [
            {"name": "Recipe 1", "link": "/recipe/1"}
            {"name": "Recipe 2", "link": "/recipe/2"}
        ]
    }
    return render(request, 'recipe_list.html', ctx)

def recipe_1(request):
    ctx = {"recipe": recipes["recipe1"]}
    return render(request, 'recipe_1', ctx)

def recipe_2(request):
    ctx = {"recipe": recipes["recipe2"]}
    return render(request, 'recipe_2.html', ctx)