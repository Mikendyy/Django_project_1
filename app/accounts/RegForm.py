import uuid

from accounts.models import User
from django import forms


class UserFormForCreate(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password1"] != cleaned_data["password2"]:
            raise forms.ValidationError("Wrong!!")
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = str(uuid.uuid4())
        instance.set_password(self.cleaned_data["password1"])
        instance.is_active = False
        from accounts.utils_active import fun_send_mail_to_active
        from django.urls import reverse
        fun_send_mail_to_active(
            # active_link=f"http://127.0.0.1:8000/{reverse(k'accounts:activated-link', args=[instance.username])}",
            active_link=f"http://127.0.0.1:8000/accounts/activet/{instance.username}",

            active_mail=instance.email

        )

        if commit:
            instance.save()
        return instance
