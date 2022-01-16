# Generated by Django 3.2.10 on 2022-01-16 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20220115_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PackageItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=20)),
                ('package', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.package')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.products')),
            ],
        ),
        migrations.DeleteModel(
            name='Packages',
        ),
    ]
