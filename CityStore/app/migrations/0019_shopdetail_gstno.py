# Generated by Django 3.0.3 on 2020-08-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200810_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetail',
            name='gstno',
            field=models.CharField(default='Not Available', max_length=40, null=True),
        ),
    ]
