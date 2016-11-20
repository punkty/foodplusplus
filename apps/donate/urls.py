from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='donor_home'),
    url(r'^foodbank$', views.index, name='foodbank_home'),
    url(r'^add_offer$', views.add_offer, name='add_offer'),
    url(r'^add_request$', views.add_request, name='add_request'),
    url(r'^fulfill/(?P<item_id>\d+)$', views.fulfill, name='fulfill'),
    url(r'^claim/(?P<item_id>\d+)$', views.claim, name='claim'),
    url(r'^recieved/(?P<item_id>\d+)$', views.recieved, name='recieved'),
    url(r'^cancel/(?P<item_id>\d+)$', views.cancle, name='cancel'),
    url(r'^show_donater/(?P<user_id>\d+)$', views.show_donater, name='show_donater'),
    url(r'^show_foodbank/(?P<user_id>\d+)$', views.show_foodbank, name='show_foodbank'),
    url(r'^show_all$', views.show_all, name='show_all'),
    url(r'^logout$', views.logout, name='logout')
  ]