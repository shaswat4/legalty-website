
from django.urls import path
from .views import SignupView , displayProfile

urlpatterns = [
    path('signup/', SignupView.as_view() , name= 'register'),
    path('<int:pk>', displayProfile , name= 'display-profile'),
]
