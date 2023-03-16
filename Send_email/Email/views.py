from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def Email_view(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail( 
            name,
            message, 
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
         )
    return render(request, template_name='index.html')