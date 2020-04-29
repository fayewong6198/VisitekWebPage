from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


def contact(request):
    if (request.method == "POST"):
        print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCc")
        name = request.POST.get("name", "")
        subject = request.POST.get("subject", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        message = request.POST.get("message", "")
        contact = Contact(name=name, subject=subject,
                          email=email, phone=phone, message=message)
        contact.save()

        return redirect('/contact')
