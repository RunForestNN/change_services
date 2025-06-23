"""
URL configuration for testJob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path, include


from workTest import views

urlpatterns = [
    path("", include("workTest.urls")),
    path("admin/", admin.site.urls),
    path("ad_card/<int:pk>/", views.ad_card, name="ad_card"),
    path("create_ad/", views.create_ad, name="create_ad"),
    path("person_page/<int:pk>/", views.person_page, name="person_page"),
    path("edit_ad/<int:pk>/", views.edit_ad, name="edit_ad"),
    path("create_offer/<int:ad_id>/", views.create_offer, name="create_offer"),
    path(
        "create_offer/<int:offer_id>/<str:action>/",
        views.manage_offer,
        name="manage_offer",
    ),
    path("delete_ad/<int:pk>/", views.delete_ad, name="delete_ad"),
]

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]
