# Generated by Django 3.2 on 2023-03-12 12:18

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20230118_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveIntegerField(db_index=True, validators=[reviews.validators.validate_year], verbose_name='Дата выхода'),
        ),
    ]
