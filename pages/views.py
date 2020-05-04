from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages

# Create your views here.
from blogs.models import Blog

from contact.models import Contact


def index(request):
    blogs = Blog.objects.all()

 
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if (request.method == "POST"):

        name = request.POST.get("name", "")
        subject = request.POST.get("subject", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        message = request.POST.get("message", "")
        contact = Contact(name=name, subject=subject,
                          email=email, phone=phone, message=message)
        contact.save()

        return render(request, 'pages/contact.html', {})
    return render(request, 'pages/contact.html')


def blog(request):
    blogs = Blog.objects.order_by('-created_at')[:6]

    context = {
        'blogs': blogs
    }
    return render(request, 'pages/blog/blog.html', context)


def blog1(request, id):
    blog = get_object_or_404(Blog, pk=id)

    context = {
        'blog': blog,
        'id': id
    }
    return render(request, 'pages/blog/blog1.html', context)


def blog2(request):
    return render(request, 'pages/blog/blog2.html')


def service(request):
    return render(request, 'pages/service/service.html')


def detail_service(request):
    context = {
        'status': 'detail_service',
        "active": "active"

    }
    return render(request, 'pages/service/detail-service.html', context)


def service_detail_consult(request):
    context = {
        'status': 'service_detail_consult'
    }
    return render(request, 'pages/service/service-detail-consult.html', context)


def service_detail_manage(request):
    context = {
        'status': 'service_detail_manage'
    }
    return render(request, 'pages/service/service-detail-manage.html', context)


def service_detail_repair(request):
    context = {
        'status': 'service_detail_repair'
    }
    return render(request, 'pages/service/service-detail-repair.html', context)


def service_detail_security(request):
    context = {
        'status': 'service_detail_security'
    }
    return render(request, 'pages/service/service-detail-security.html', context)


def service_detail_outsource(request):
    context = {
        'status': 'service_detail_outsource'
    }
    return render(request, 'pages/service/service-detail-outsource.html', context)
