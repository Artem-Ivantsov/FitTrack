from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dish, SportRecipe, Food, FoodSelection
from .forms import DishForm

@login_required
def my_dishes_view(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.user = request.user
            dish.save()
            return redirect('my_dishes')
    else:
        form = DishForm()

    
    dishes = Dish.objects.filter(user=request.user)

    return render(request, 'food/my_dishes.html', {
        'form': form,
        'dishes': dishes
    })

def sport_recipes_view(request):
    recipes = SportRecipe.objects.all()
    return render(request, 'food/sport_recipes.html', {'recipes': recipes})

@login_required
def special_menu(request):
    foods = Food.objects.all()

    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        if food_id:
            food = Food.objects.get(id=food_id)
            FoodSelection.objects.create(user=request.user, food=food)
            return redirect('my_selection')

    return render(request, 'food/special_menu.html', {'foods': foods})

@login_required
def my_selection(request):
    selections = FoodSelection.objects.filter(user=request.user)
    return render(request, 'food/my_selection.html', {'selections': selections})