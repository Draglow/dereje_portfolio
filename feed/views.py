from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from . forms import ContactForm
from .forms import CVForm
from .models import CV



# Create your views here.
def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }

    return render(request, 'feed/home_page.html', context)
from django.contrib import messages
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message_body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            send_mail('New message from your website', message_body, email, ['draglow21@gmail.com']) 
            messages.success(request, 'Your message has been sent successfully.')  # Add success message
            return render(request, 'feed/contact.html')  
        else:
            messages.error(request, 'There was an error in the form submission.')  # Add error message
    else:
        form = ContactForm()
    return render(request, 'feed/contact.html', {'form': form, 'disable_nav_links': True})



def upload_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cv_uploaded')
    else:
        form = CVForm()
    return render(request, 'feed/upload_cv.html', {'form': form})

def download_cv(request):
    cv = CV.objects.first()  # Assuming there's only one CV in the database
    messages.info(request, 'The download process has started.')
    return redirect(cv.pdf.url)