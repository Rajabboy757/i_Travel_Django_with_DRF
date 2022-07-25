from django.db import models
from django.contrib.auth.models import AbstractUser
# from iTravel.tours.models import Tour

months_choice =(
("1","Январь"),
("2","Февраль"),
("3","Март"),
("4","Апрель"),
("5","Май"),
("6","Июнь"),
("7","Июль"),
("8","Август"),
("9","Сентябрь"),
("10","Октябрь"),
("11","Ноябрь"),
("12","Декабрь"),
)

date = models.CharField(max_length=3,
    choices=months_choice)

class CustomUser(AbstractUser):
    birth_day = models.PositiveIntegerField(blank=True, null=True, default=1)
    birth_month = models.CharField(choices=months_choice, default=months_choice[0], max_length=20)
    birth_year = models.PositiveIntegerField(blank=True, null=True, default=2000)
    phone = models.CharField(max_length=13)
    # tours = models.ForeignKey(Tour, on_delete=models.CASCADE())

