# Generated by Django 2.2.7 on 2019-12-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0007_auto_20191209_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
