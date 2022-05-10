from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivateUserAccount.as_view(),
         name='activate_account'),
    path('login/', views.LoginAPIView.as_view()),
   # path('logout/', views.Logout.as_view()),
]