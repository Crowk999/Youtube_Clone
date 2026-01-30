from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return redirect("/")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, (f"Welcome, {user.username}!"))
        return redirect("/")