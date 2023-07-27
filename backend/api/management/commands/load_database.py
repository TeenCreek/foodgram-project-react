import json

from django.core.management import BaseCommand

from recipes.models import Ingredient, Tag


class Command(BaseCommand):
    """Загрузка данных из json файла."""

    def handle(self, *args, **options):
        self.fill_ingredients()
        self.fill_tags()

    def fill_ingredients(self):
        with open('./data/ingredients.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        for row in data:
            ingredient, _ = Ingredient.objects.update_or_create(
                name=row['name'],
                defaults={'measurement_unit': row['measurement_unit']}
            )
            ingredient.save()

    def fill_tags(self):
        with open('./data/tags.json', 'r', encoding='utf-8') as t:
            data = json.load(t)

        for row in data:
            tag, _ = Tag.objects.update_or_create(
                name=row['name'],
                defaults={'color': row['color'], 'slug': row['slug']}
            )
            tag.save()
