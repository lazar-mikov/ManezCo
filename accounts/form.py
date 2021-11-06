from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Adult,Child,Admin

class DateInput(forms.DateInput):
    input_type = "date"

class AdultSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    date = forms.CharField(widget=DateInput)

    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_adult = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.date = self.cleaned_data.get('date')
       
        user.save()
        adult = Adult.objects.create(user=user)
        adult.phone_number=self.cleaned_data.get('phone_number')
        adult.location=self.cleaned_data.get('location')
        adult.save()
        return user

class ChildSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_child = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        child = Child.objects.create(user=user)
        child.phone_number=self.cleaned_data.get('phone_number')
        child.designation=self.cleaned_data.get('designation')
        child.save()
        return user

class AdminSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        admin = Admin.objects.create(user=user)
        admin.phone_number=self.cleaned_data.get('phone_number')
        admin.designation=self.cleaned_data.get('designation')
        admin.save()
        return user
