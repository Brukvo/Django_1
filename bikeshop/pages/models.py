from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    desc = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='товар', max_length=128)
    img = models.ImageField(verbose_name='изображение', upload_to='product_images', blank=True)
    short = models.CharField(verbose_name='краткое описание', max_length=60, blank=True)
    desc = models.TextField(verbose_name='подробное описание', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} / {self.category.name}'
