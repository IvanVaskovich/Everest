# Generated by Django 4.1.3 on 2022-11-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_trademark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Старая цена'),
        ),
    ]
