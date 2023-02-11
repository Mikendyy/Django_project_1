from django.contrib import admin
from django.urls import path, include
from customers.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home-link"),
    path('', include('customers.urls')),
    path("accounts/", include("accounts.urls")),
    path('auth/', include('django.contrib.auth.urls')),
]
