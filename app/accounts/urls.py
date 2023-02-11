from django.contrib import admin
from django.urls import path
from accounts.views import UserRegView
from accounts.views import ActivatedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', UserRegView.as_view(), name="registration-link"),
    path('activated/<uuid:username>', ActivatedView.as_view(), name='activated-link'),
]