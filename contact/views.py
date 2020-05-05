from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contact
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def contact(request):
    if (request.method == "POST"):
        a = request.POST.dict()
        name = a.get("name")
        subject = a.get("subject")
        email = a.get("email")
        message = a.get("message")
        #phone = a.get("phone")
        contact = Contact(name=name, subject=subject,
                          email=email, message=message)
        contact.save()
        print(request.path)
        messages.success(request, "Your message have been saved.")
        return render(request, "pages/index.html")

    return redirect('/')


def consult(request):
    if (request.method == "POST"):
        a = request.POST.dict()
        name = a.get("name1")
        subject = a.get("subject1")
        email = a.get("email1")
        message = a.get("message1")
        phone = a.get("phone1")
        contact = Contact(name=name, subject=subject,
                          email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your message have been saved.")
        return render(request, "pages/index.html")

    return redirect('/')
