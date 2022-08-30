from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Наименование'
    )
    measurement_unit = models.CharField(max_length=100,
                                        verbose_name='Единицы измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Наименование'
    )
    color = ColorField(verbose_name='Цвет')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes'
    )
    name = models.CharField(max_length=200,
                            verbose_name='Название')
    image = models.ImageField(
        upload_to='recipes/images/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    text = models.TextField(verbose_name='Рецепт')
    ingredients = models.ManyToManyField(
            Ingredient,
            through='IngredientRecipe',
            verbose_name='Ингредиенты',
            related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag,
        through='TagRecipe',
        verbose_name='Тэги',
        related_name='recipes')
    cooking_time = models.PositiveIntegerField(
            validators=[MinValueValidator(1), ],
            verbose_name='Время приготовления'
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )
    measurement_unit = models.CharField(max_length=50,
                                        verbose_name='Единицы измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name