from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [ 
    path('register', views.createuser, name='index'),
    path('category',views.registercategory),
    path('brand',views.registerbrand),
    path('addproduct',views.registerproduct),
    path('login',views.loginuser),
    path('token',TokenObtainPairView.as_view),
    path('refresh', TokenRefreshView.as_view),
]