import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFintessPal.settings')
django.setup()

from food.models import SportRecipe 

with open('static\json\sport_recipes.json', encoding='utf-8') as f:
    data = json.load(f)


for item in data:
    SportRecipe .objects.create(
        name=item['name'],
        calories=item['calories'],
        protein=item['protein'],
        fat=item['fat'],
        carbs=item['carbs']
    )

print("✅ Записей:", len(data))
