from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import RedirectView
from accounts.models import User
from accounts.RegForm import UserFormForCreate


class UserRegView(CreateView):
    model = User
    form_class = UserFormForCreate
    success_url = reverse_lazy("home-link")
    template_name = 'registration.html'

    # def form_valid(self, form):
    #     from django.contrib import messages
    #     messages.info(self.request,"Thanks for reg!")
    #     return super().form_valid(form)


class ActivatedView(RedirectView):
    pattern_name="home-link"


    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop("username")
        user = get_object_or_404(User,usename=username,is_active=False)
        user.is_active=True
        user.save(update_filds=("is_active",))

        user.refresh_from_db()
        return super().get_redirect_url(*args,**kwargs)