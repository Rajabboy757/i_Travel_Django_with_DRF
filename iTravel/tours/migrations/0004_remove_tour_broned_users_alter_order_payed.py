# Generated by Django 4.0.6 on 2022-07-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_remove_tour_broned_tours_tour_broned_users_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='broned_users',
        ),
        migrations.AlterField(
            model_name='order',
            name='payed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
