
from django.contrib import admin
from django.urls import include, path
from shop.views import admpanel_view, custom_logout, main_page
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', main_page, name='main'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admpanel/', admpanel_view, name="admin"),
    path('admpanel/custom_logout/', custom_logout, name='custom_logout'),
    path('custom_logout/', custom_logout, name='custom_logout'),
]
