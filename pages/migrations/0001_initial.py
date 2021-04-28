# Generated by Django 3.0 on 2021-03-02 11:56

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('product_photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('product_photo_1', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('product_photo_2', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('product_photo_3', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('product_photo_4', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('sku', models.IntegerField()),
                ('category', models.CharField(choices=[('Shoes', 'Shoes'), ('Clothes', 'Clothes'), ('Watches', 'Watches'), ('Electronics', 'Electronics')], max_length=50)),
                ('brand', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
