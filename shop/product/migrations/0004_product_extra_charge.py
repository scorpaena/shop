# Generated by Django 3.2 on 2021-07-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_procurement_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='extra_charge',
            field=models.PositiveIntegerField(default=0),
        ),
    ]