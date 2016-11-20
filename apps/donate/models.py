from __future__ import unicode_literals
from ..login.models import User
from django.db import models


class ItemManager(models.Manager):
    def add_offer:
        pass
    
    
        
        


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    foodbank = models.ForeignKey(User,related_name='item_requests')
    donor = models.ForeignKey(User,related_name='item_offers')
    active = models.BooleanField(initial=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()