# Generated by Django 4.0.2 on 2022-03-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('items', models.TextField()),
                ('price', models.IntegerField()),
                ('products_name', models.TextField()),
                ('product_type', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
