from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('receive/', receive, name='show'),
    path('subscribe/<int:pk>/', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>/', unsubscribe, name='unsubscribe'),
    path('add_ntf_templates/', ntf_templates_view, name='add_ntf_templates')

]
