from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_item$', views.add_item, name='add_item'),
    url(r'^destroy_item/(?P<item_id>\d+)$', views.destroy_item, name='destroy_item'),
    url(r'^fulfill/(?P<item_id>\d+)/(?P<user_id>\d+)$', views.fulfill, name='fulfill'),
    url(r'^claim/(?P<item_id>\d+)$', views.claim, name='claim'),
    url(r'^received/(?P<item_id>\d+)$', views.received, name='received'),
    url(r'^cancel/(?P<item_id>\d+)$', views.cancel, name='cancel'),
    url(r'^show_user/(?P<user_id>\d+)$', views.show_user, name='show_user'),
    url(r'^show_all$', views.show_all, name='show_all'),
    url(r'^accepted/(?P<item_id>\d+)$', views.accepted, name='accepted'),
    url(r'^logout$', views.logout, name='logout')
  ]
