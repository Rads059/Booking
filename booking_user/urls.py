from django.urls import path
from .views import Login,Register,AdviserView,BookingView

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('<int:user_id>/advisor/',AdviserView.as_view()),
    path('<int:user_id>/advisor/booking/',BookingView.as_view()),
    path('<int:user_id>/advisor/<int:advisor_id>/',BookingView.as_view()),

]