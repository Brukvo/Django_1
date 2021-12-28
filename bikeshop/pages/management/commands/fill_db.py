import os
import json

from django.core.management.base import BaseCommand

from authapp.models import CommonUser
from mainapp.models import Category, Product
from django.conf import settings


def load_from_json(file_name):
    with open(
            os.path.join(settings.JSON_PATH, f'{file_name}.json'),
            encoding='utf-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Заполняет БД данными'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        [Category.objects.create(**category) for category in categories]

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category = product['category']
            # Получаем категорию по имени
            _category = Category.objects.get(name=category)  # .get() -> concrete object
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = CommonUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
