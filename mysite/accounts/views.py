from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser
from django.contrib.auth import login
from django.views.generic import DetailView
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
        return render(request, 'accounts/register.html', {'form': form})




class ProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'
    slug_field = 'username'
    slug_url_kwarg = 'username'