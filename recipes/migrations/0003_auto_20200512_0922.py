# Generated by Django 3.0.6 on 2020-05-12 12:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20200512_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='food_type',
            field=models.CharField(blank=True, choices=[('FAS', 'Fast Food'), ('DOC', 'Doce'), ('BRA', 'Brasileira'), ('ASI', 'Asiática')], max_length=5),
        ),
    ]
