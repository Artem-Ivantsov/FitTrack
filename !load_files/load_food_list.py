import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFintessPal.settings')
django.setup()

from food.models import Food

with open('static\json\food_list_100.json', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    Food.objects.create(
        name=item['name'],
        serving_size=item['serving_size'],
        calories=item['calories'],
        protein=item['protein'],
        carbs=item['carbs'],
        fat=item['fat'],
        sugar=item['sugar'],
        sodium=item['sodium'],
        fiber=item['fiber']
    )

print("✅ Записей:", len(data))
