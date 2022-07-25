# Generated by Django 4.0.6 on 2022-07-20 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_tour_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='broned_tours',
        ),
        migrations.AddField(
            model_name='tour',
            name='broned_users',
            field=models.JSONField(default=dict),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payed', models.BooleanField(default=False)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='tours.tour')),
            ],
        ),
    ]
