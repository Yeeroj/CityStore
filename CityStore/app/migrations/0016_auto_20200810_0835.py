# Generated by Django 3.0.4 on 2020-08-10 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200810_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shopname',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ShopDetail'),
        ),
    ]
