from django.shortcuts import render, redirect
from ..login.models import User
from .models import Item

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    #will display a dasboard depending on which type of user is logged in
    if not session_check(request):
        return redirect('login:index')

    if request.session['user']['user_type'] == 1:
        context = {
            'foodbank_items': Item.objects.filter(foodbank__id=request.session['user']['user_id'])
        }
        return render(request, 'donate/index_foodbank.html', context)

    elif request.session['user']['user_type'] == 0:
        context = {
            'donor_items': Item.objects.filter(donor__id=request.session['user']['user_id'])
        }
        return render(request, 'donate/index_donor.html', context)

def add_item(request):
    #creates a offer from a donor
    if not session_check(request):
        return redirect('login:index')

    if request.session['user']['user_type'] == 1:
        Item.objects.add_request(request)

    elif request.session['user']['user_type'] == 0:
        Item.objects.add_offer(request)
    
    return redirect('donate:index')

def fulfill(request, item_id):
    # updates item's donor foreign key
    if not session_check(request):
        return redirect('login:index')

def claim(request, item_id):
    # updates an item's foodbank foreign key
    if not session_check(request):
        return redirect('login:index')

def recieved(request, item_id):
    # sets item's active = 0, adds to donations count for donor
    if not session_check(request):
        return redirect('login:index')

def cancel(request, item_id):
    #allows foodbank to reject a fulfillment
    if not session_check(request):
        return redirect('login:index')

def show_donor(request, user_id):
    #renders donors page featuring completed donations and current offers
    if not session_check(request):
        return redirect('login:index')

def show_foodbank(request, user_id):
    #renders foodbank page featuring current items requested and location?
    if not session_check(request):
        return redirect('login:index')

def show_all(request):
    #shows queries on whats available based on user type
    if not session_check(request):
        return redirect('login:index')

def logout(request):
    request.session.clear()

    return redirect('login:index')
