from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('receive/', receive, name='show'),
    # path('send_to_microservice/', send_to_microservice, name='send_to_microservice'),
    path('add_ntf_templates/', ntf_templates_view, name='add_ntf_templates')


]
