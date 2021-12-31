# Generated by Django 3.2.10 on 2021-12-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_cart_q'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.products')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='q',
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='users.CartItems'),
        ),
    ]