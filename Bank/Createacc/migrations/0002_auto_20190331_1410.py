# Generated by Django 2.1.7 on 2019-03-31 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Createacc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='fname',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='lname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='data',
            name='password',
            field=models.CharField(default='0000', max_length=4, unique=True),
        ),
    ]