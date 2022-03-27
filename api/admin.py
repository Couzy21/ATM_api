from django.contrib import admin
from .models import Agents, Account, Customer
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
User = get_user_model()
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username','is_staff',]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Agents)
admin.site.register(Account)
admin.site.register(Customer)
