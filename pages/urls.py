from django.urls import path
from.views import about_view,services_view,blog_view,cart_view,checkout_view,index_view,shop_view,thankyou_view,contact_view

urlpatterns=[
    path('about/',about_view),
    path('',index_view),
    path('services/',services_view),
    path('blog/',blog_view),
    path('cart/',cart_view),
    path('checkout/',checkout_view),
    path('shop/',shop_view),
    path('thankyou/',thankyou_view),
    path('contact us/',contact_view)



]