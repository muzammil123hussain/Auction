
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class User(AbstractUser):
    pass

class Category(models.Model):
    category = CharField(max_length=50, null=False)

class listings(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, default='1')
    title = models.CharField(max_length=50 , null=False, unique=True)
    description = models.CharField(max_length=100, null=False, default='ABC')
    starting_price = models.IntegerField(null=False , default='123')
    category = models.ForeignKey(Category, on_delete=CASCADE, null=False, default='1')
    active = models.BooleanField(null=False, default=False)


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, default='1')
    auction = models.ForeignKey(listings, on_delete=CASCADE, null=False, default='1')
    bid_price = models.IntegerField(null=False, default='1000')
    bid_time = models.TimeField(null=False, default='00:00:00')

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, default='1')
    auction = models.ForeignKey(listings, on_delete=CASCADE, null=False, default='1')
    comments = models.CharField(max_length=150, default='abc')

class watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE,)
    auction = models.ForeignKey(listings, on_delete=CASCADE)
    active = models.BooleanField(default=False)




