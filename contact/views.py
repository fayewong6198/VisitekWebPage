from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contact
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def newContact(request):
    if (request.method == "POST"):
        a = request.POST.dict()
        name = a.get("name")
        subject = a.get("subject")
        email = a.get("email")
        message = a.get("message")
        phone = a.get("phone")
        contact = Contact(name=name, subject=subject,
                          email=email, message=message, phone=phone)
        contact.save()
        messages.success(request, "Your contact have been saved.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        storage = messages.get_messages(request)
        storage.used = True
    messages.success(request, "server error")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
