from . import views
from .models import Profile
from django.urls import path

from .views import ProfileUpdate

urlpatterns = [
    path("<int:pk>/",  views.ProfileDetail.as_view(), name="profile-detail"),
    # path("<slug:slug>/",  views.ProfileDetail.as_view(), name="profile-detail"),
    path('<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),

]