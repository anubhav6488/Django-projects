# Generated by Django 4.1 on 2022-10-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_NAME', models.CharField(max_length=50)),
                ('category_NAME', models.CharField(max_length=50)),
                ('Subcategory', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('dis', models.CharField(max_length=50)),
                ('publish_date', models.DateField(blank=True)),
                ('publish_image', models.FileField(default=None, max_length=250, null=True, upload_to='products/')),
            ],
        ),
    ]
