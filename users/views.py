from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def register_view(request):
    # form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username =  form.cleaned_data.get('username')
            print(username)
            # messages.add_message(request,messages.success,f'account {username} is created')
            messages.success(request,f'{username} created')
            return redirect('structure:home')
    form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    fields =['first_name','last_name','email']
    model = Profile
    template_name = 'users/profile_view.html'
    success_url = reverse_lazy('users:profile')
    def get_object(self,**kwargs):
        user = self.request.user
        # if user is None:
        #     reaise Http404
        return get_object_or_404(Profile,user = user)
