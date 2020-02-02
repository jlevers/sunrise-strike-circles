# Generated by Django 3.0.2 on 2020-02-02 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strikecircle', '0010_auto_20200120_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='date_collected',
            field=models.DateField(choices=[(datetime.date(2020, 2, 17), 'Week 2'), (datetime.date(2020, 2, 24), 'Week 3'), (datetime.date(2020, 3, 2), 'Week 4'), (datetime.date(2020, 3, 9), 'Week 5'), (datetime.date(2020, 3, 16), 'Week 6'), (datetime.date(2020, 3, 23), 'Post Strike Circle')]),
        ),
    ]