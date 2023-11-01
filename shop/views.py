from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Order

def main_page(request):
    orders = Order.objects.all()
    return render(request, 'templates/shop/index.html', {'orders': orders})

@login_required
def admpanel_view(request):
    orders = Order.objects.all()
    return render(request, 'templates/shop/admin-panel.html', {'orders': orders})

def custom_logout(request):
    logout(request)
    return redirect('main')