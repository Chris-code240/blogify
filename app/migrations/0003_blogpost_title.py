# Generated by Django 4.2.3 on 2023-08-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]