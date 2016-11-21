from __future__ import unicode_literals
from ..login.models import User
from django.db import models


class ItemManager(models.Manager):
    def add_offer(self, request):
        user = User.objects.get(id=request.session['user']['user_id'])
        Item.objects.create(name=request.POST['name'], description=request.POST['description'], donor=user,owner=user)
    
    def add_request(self, request):
        user = User.objects.get(id=request.session['user']['user_id'])
        item = Item.objects.create(name=request.POST['name'], description=request.POST['description'], foodbank=user,owner=user)
        print "*"*80
        print item.name
        print item.owner.name
    
    def destroy_item(self, request, item_id):
        Item.objects.get(id=item_id).delete()
        
    def fulfill(self, request, item_id):
        user = User.objects.get(id=request.session['user']['user_id'])
        item = Item.objects.get(id=item_id)
        item.donor = user
        item.save()

    def claim(self, request, item_id):
        user = User.objects.get(id=request.session['user']['user_id'])
        item = Item.objects.get(id=item_id)
        item.foodbank = user
        item.save()

    def received(self, request, item_id):
        item = Item.objects.get(id=item_id)
        item.active = False
        user = User.objects.get(id=item.donor.id)
        user.donations += 1
        user.save()
        item.save()

    def cancel(self, request, item_id):
        item = Item.objects.get(id=item_id)
        if item.owner.user_type == 0:
            item.foodbank = None
            item.save()
        elif item.owner.user_type == 1:
            item.donor = None
            item.save() 

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    foodbank = models.ForeignKey(User, related_name='item_requests', null=True)
    donor = models.ForeignKey(User, related_name='item_offers', null=True)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, related_name='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ItemManager()
