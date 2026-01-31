from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


def home(request):

    context = {}
    return render(request, 'aii/home.html', context)



def inquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        subject = f"New Contact Enquiry: {service}"
        body = f"""
        New enquiry from AIIS website

        Name: {name}
        Email: {email}
        Phone: {phone}
        Service: {service}

        Message:
        {message}
        """

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['winniesimone1@gmail.com'],  # RECEIVER EMAIL
            fail_silently=False,
        )

        return redirect('home')

    return render(request, 'aii/inquiry.html')
