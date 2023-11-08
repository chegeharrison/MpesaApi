from django.urls import path
from . import views
from .views import payment_view

urlpatterns = [
    # path('', views.index, name='Index'),
    path('payment/', payment_view, name='payment'),
]