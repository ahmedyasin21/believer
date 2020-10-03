from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from .forms import UserCreateForm
from django.views.generic import CreateView,TemplateView,View
from . import forms
from islamic import settings
from django.contrib.auth.models import User
from .forms import ContactForm
# email 
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib import messages

# import random
# user = User

# token = 3
class SignUp(CreateView):
    form_class = UserCreateForm
    template_name = 'accounts/signup.html'
        
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Believer Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('accounts:verify')

        return render(request, self.template_name, {'form': form})

class VerifyEmailView(TemplateView):
    template_name = "accounts/verified.html"

 
class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('accounts:login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')



class ContactView(CreateView):
    template_name = "accounts/contact.html"
    form_class = ContactForm

    def form_valid(self, form,*args, **kwargs):

        from_user = self.request.user
        print(from_user)
        to_user = form.cleaned_data["to_user"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        if form.is_valid:
            send_mail(
                subject,
                message,
                from_user,
                [to_user],
                fail_silently=False,
                )  
        
        return super(*args, **kwargs).form_valid(form)

class SentView(TemplateView):
    template_name = 'accounts/sent_confirm.html'   

   
   
        
 






# class ProfileView(TemplateView):
#     template_name = "accounts/userprofile.html"




# @login_required
# def userprofile(request):
#     u_form =UserUpdateForm
#     p_form = UserProfileForm()

#     context ={
#         'u_form':u_form,
#         'p_form' :p_form
#     }
#     return render(request,"accounts/userprofile.html")





    



