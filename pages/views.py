from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from unidecode import unidecode
# Create your views here.
from blogs.models import Blog, Category
from contact.models import Contact


def index(request):
    blogs = Blog.objects.all().order_by('-created_at')[:3]

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


def blog_detail(request, id):
    blog = Blog.objects.get(pk=id)
    category = Category.objects.all()

    related = Blog.objects.filter(
        category=blog.category).exclude(pk=id)
    recent = Blog.objects.order_by('-created_at')[:15]
    context = {
        'blog': blog,
        'id': id,
        'related': related,
        'category': category,
        'recent': recent
    }
    print(context)
    return render(request, 'pages/blog/blog_detail.html', context)


def listBlog(request):
    blogs = Blog.objects.order_by('-created_at')[:6]
    category = Category.objects.all()
    recent = Blog.objects.order_by('-created_at')[:15]
    context = {
        'blogs': blogs,
        'category': category,
        'recent': recent
    }
    return render(request, 'pages/blog/listBlog.html', context)


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


def search(request):
    content = unidecode(request.GET.get('search')).split()
    result = []
    blogs = Blog.objects.all()
    for i in content:
        for x in blogs:
            if x not in result:
                if i.lower()in unidecode(x.title).lower():
                    result.append(x)

    context = {
        'blogs': result
    }
    return render(request, 'pages/blog/listBlog.html', context)
