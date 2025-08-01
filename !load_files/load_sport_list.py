import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFintessPal.settings')
django.setup()

from exercises.models import Exercise

with open('static\json\sport_list.json', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    Exercise.objects.create(
        name=item['name'],
        muscle_group=item['muscle_group'],
        equipment=item['equipment'],
        type=item['type'],
    )

print("✅ Записей:", len(data))
