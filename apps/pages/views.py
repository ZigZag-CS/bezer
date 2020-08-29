from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .models import *
from .forms import *

@login_required(login_url='/')
def dash_page(request):
    content_list = Contet.objects.all()
    context = {'list': content_list}
    return render(request, 'dashboard.html', context)


class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/dash/'
    template_name = 'login.html'
    default_next = '/dash/'

    def form_valid(self, form):
        print("form valid in LoginView")
        next_path = self.get_next_url()
        print(f'LoginView : def form_valid - next_path: {next_path}')
        return redirect(next_path)


def user_logout(request):
    auth.logout(request)
    return redirect('/')