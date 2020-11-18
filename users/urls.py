
from django.urls import path
from .views import SignupView , displayProfile , CreateLawyerProfile  , EditLawyerProfile
from .views import reviewDisplay

urlpatterns = [
    path('signup/', SignupView.as_view() , name= 'register'),
    path('<int:pk>', displayProfile , name= 'display-profile'),
    path('<int:pk>/create', CreateLawyerProfile.as_view() , name= 'create-profile'),
    path('<int:pk>/edit', EditLawyerProfile.as_view() , name= 'edit-profile'),
    #path('u/<int:pk>', detailLawyer , name= 'det'),
    path('<int:pk>/review', reviewDisplay , name= 'review'),
]
