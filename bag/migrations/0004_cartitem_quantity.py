# Generated by Django 4.1.4 on 2023-07-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0003_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]