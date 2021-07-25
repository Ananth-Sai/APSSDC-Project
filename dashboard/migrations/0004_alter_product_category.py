# Generated by Django 3.2.4 on 2021-07-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food'), ('Medical', 'Medical'), ('Tools', 'Tools')], max_length=20, null=True),
        ),
    ]