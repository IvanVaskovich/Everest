# Generated by Django 4.1.3 on 2022-11-03 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_category_category_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentcategory',
            name='parent_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ParentCategory',
        ),
    ]