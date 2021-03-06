# Generated by Django 3.2.9 on 2022-01-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20220114_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tag',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
