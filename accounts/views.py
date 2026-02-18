from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from .forms import RegisterForm
from .models import CustomUser


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'accounts/login.html'



class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'