from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, CreateUserForm

# Create your views here.

#class UserRegisterView(generic.CreateView):
#    form_class = UserCreationForm
#    template_name = 'registration/register.html'
#    success_url = reverse_lazy('login')

def registerPage(request):
    #form = UserCreationForm()
    form = CreateUserForm()
    

    if request.method == 'POST':
       # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
       
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request,'registration/register.html', context)


def loginPage(request):
    return render(request,'registration/login.html', {})

##########
#NotUsing#
##########
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
##########
#NotUsing#
##########
