# Generated by Django 2.2.7 on 2019-12-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0006_auto_20191129_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='Shift',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='runs_from',
        ),
        migrations.AddField(
            model_name='squirrel',
            name='runs_fro',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(choices=[('pm', 'PM'), ('am', 'AM')], default='am', max_length=5),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', 'N/A')], default='adult', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='approaches',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='indifferent',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='kuks',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(choices=[('above ground', 'Above Ground'), ('ground plane', 'Ground Plane'), ('', 'N/A')], default='above ground', max_length=50),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(choices=[('black', 'Black'), ('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('', 'N/A')], default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]