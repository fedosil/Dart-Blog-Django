# Generated by Django 4.1.3 on 2022-12-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pinned_to',
            field=models.BooleanField(default=False, verbose_name='Закрепить на главной'),
        ),
    ]
