# Generated by Django 2.2.9 on 2020-01-14 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strikecircle', '0007_auto_20200113_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='data_collected',
            new_name='date_collected',
        ),
        migrations.RemoveField(
            model_name='pledge',
            name='one_on_one',
        ),
    ]