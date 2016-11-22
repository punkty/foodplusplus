from django.shortcuts import render, redirect, HttpResponse
from ..login.models import User
from .models import Item
from django.contrib import messages

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    # will display a dasboard depending on which type of user is logged in
    if not session_check(request):
        return redirect('login:index')

    if request.session['user']['user_type'] == 1:
        context = {
            'foodbank_items': Item.objects.filter(foodbank__id=request.session['user']['user_id']),
            'available_items': Item.objects.filter(foodbank__isnull=True),
        }
        return render(request, 'donate/index_foodbank.html', context)

    elif request.session['user']['user_type'] == 0:
        context = {
            'donation_count': User.objects.get(id=request.session['user']['user_id']),
            'donor_items': Item.objects.filter(donor__id=request.session['user']['user_id'])
        }
        return render(request, 'donate/index_donor.html', context)

def add_item(request):
    # creates a offer from a donor
    if not session_check(request):
        return redirect('login:index')

    if request.session['user']['user_type'] == 1: # item is a request if you are a foodbank
        result = Item.objects.add_request(request)

        if result: # form validation
            print_errors(request, result)
            return redirect('donate:index')

    elif request.session['user']['user_type'] == 0: # item is an offer if you are a donor
        result = Item.objects.cap_check(request)

        if result: # Active item capacity check
            print_errors(request, result)
            return redirect('donate:index')

        result = Item.objects.add_offer(request)

        if result: # form validation
            print_errors(request, result)
            return redirect('donate:index')
    
    return redirect('donate:index')

def destroy_item(request, item_id):
    # destroys an item
    if not session_check(request):
        return redirect('login:index')

    item = Item.objects.get(id=item_id)

    if item.owner.id != request.session['user']['user_id']: # cannot delete items that are not yours
        return redirect('donate:index')

    Item.objects.destroy_item(request, item_id)

    return redirect('donate:index')

def fulfill(request, item_id, user_id):
    # updates item's donor foreign key
    if not session_check(request):
        return redirect('login:index')

    result = Item.objects.cap_check(request)

    if result: # active item capacity check
        print_errors(request, result)
        return redirect('donate:show_user', user_id)

    Item.objects.fulfill(request, item_id)

    return redirect('donate:accepted', item_id)

def claim(request, item_id):
    # updates an item's foodbank foreign key
    if not session_check(request):
        return redirect('login:index')

    Item.objects.claim(request, item_id)

    return redirect('donate:index')

def received(request, item_id):
    # sets item's active = 0, adds to donations count for donor
    if not session_check(request):
        return redirect('login:index')

    Item.objects.received(request, item_id)

    return redirect('donate:index')

def cancel(request, item_id):
    # allows foodbank to reject a fulfillment, severing donor FK
    if not session_check(request):
        return redirect('login:index')

    Item.objects.cancel(request, item_id)

    return redirect('donate:index')

def show_user(request, user_id):
    #renders a user's page
    if not session_check(request):
        return redirect('login:index')

    user = User.objects.get(id=user_id)

    if user.user_type == 0:
        if request.session['user']['user_type'] == 1: # if the user they want to see is a donor and they are a foodbank
            context = {
                'donor': User.objects.get(id=user_id),
                'donor_items': Item.objects.filter(donor__id=user_id)
            }
            return render(request, 'donate/show_donor.html', context)

    elif user.user_type == 1:
        if request.session['user']['user_type'] == 0: # if the user they want to see is a foodbank and they are a donor
            context = {
                'foodbank': User.objects.get(id=user_id),
                'requested_items': Item.objects.filter(foodbank__id=user_id)
            }
            return render(request, 'donate/show_foodbank.html', context)

    return redirect('donate:index')

def show_all(request):
    # shows foodbanks and requested items
    if not session_check(request):
        return redirect('login:index')

    context = {
        'all_foodbanks': User.objects.filter(user_type=1),
        'all_items': Item.objects.filter(donor__isnull=True),
        'foodbanks_with_requests': User.objects.filter(user_type=1).filter(item_requests__donor__isnull=True).distinct()
    }
    return render(request, 'donate/show_all_donor.html', context)

def accepted(request, item_id):
    if not session_check(request):
        return redirect('login:index')

    context = {
        'item': Item.objects.get(id=item_id)
    }
    return render(request, 'donate/accepted.html', context)

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def logout(request):
    request.session.clear()

    return redirect('login:index')
