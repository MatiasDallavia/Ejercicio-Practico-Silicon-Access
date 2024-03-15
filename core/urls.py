from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserRegistration.as_view()),
    path('auth-token/', views.GetToken.as_view()),
    path('areas/', views.SinglePrivateAreaView.as_view()),
]
