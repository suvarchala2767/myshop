from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request,'about.html')

def services_view(request):
    return render(request,'services.html')

def blog_view(request):
    return render(request,'blog.html')

def cart_view(request):
    return render(request,'cart.html')

def checkout_view(request):
    return render(request,'checkout.html')

def index_view(request):
    return render(request,'index.html')

def shop_view(request):
    return render(request,'shop.html')

def thankyou_view(request):
    return render(request,'thankyou.html')

def contact_view(request):
    return render(request,'contact.html')