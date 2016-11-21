from __future__ import unicode_literals
from ..login.models import User
from django.db import models


class ItemManager(models.Manager):
    def add_offer(self, request):
        user = User.objects.get(id=request.session['user']['user_id'])
        Item.objects.create(name=request.POST['name'], description=request.POST['description'], donor=user)
    
    def add_request(self, request):
        user = User.objects.get(id=request.session['user']['user_id'])
        Item.objects.create(name=request.POST['name'], description=request.POST['description'], foodbank=user) 
    
        
        


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    foodbank = models.ForeignKey(User,related_name='item_requests', null=True)
    donor = models.ForeignKey(User,related_name='item_offers', null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()
