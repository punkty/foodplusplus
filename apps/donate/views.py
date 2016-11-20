from django.shortcuts import render, redirect

def index(request):
    #will display a dasboard depending on which type of user is logged in
    pass

def add_offer(request):
    #creates a offer from a donter
    pass

def add_request(request):
    #creates a request for a foodbank
    pass

def fulfill(request, item_id):
    #updates a donater foreign key to item
    pass

def claim(request, item_id):
    # allows a foodbank to claim offered items
    pass

def recieved(request, item_id):
    #updates item's active state and completes donation
    pass

def cancel(request, item_id):
    #allows foodbank to reject a fulfillment
    pass

def show_donor(request, user_id):
    #renders donors page featuring completed donations and current offers
    pass

def show_foodbank(request, user_id):
    #renders foodbank page featuring current items requested and location?
    pass

def show_all(request):
    #shows queries on whats available based on user type
    pass

