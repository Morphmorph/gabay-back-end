# Generated by Django 4.2.6 on 2023-10-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_income_color_income_icon_transaction_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='icon',
            field=models.CharField(max_length=125, null=True),
        ),
    ]
