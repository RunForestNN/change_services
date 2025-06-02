from . import views, admin
from django.urls import path



urlpatterns=[
    path("", views.index, name='index'),
    path("ad_card/", views.ad_card, name='ad_card'),
    path("person_page/",views.person_page,name='person_page'),
    path("accounts/register/",views.register,name='register'),
    path("edit_ad/",views.edit_ad,name='edit_ad'),
    path("create_ad/",views.create_ad,name='create_ad'),
    path("create_offer/",views.create_offer,name='create_offer'),
    path('delete_ad/',views.delete_ad,name='delete_ad'),

]