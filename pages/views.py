from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from unidecode import unidecode
import math
# Create your views here.
from blogs.models import Blog, Category
from contact.models import Contact


def index(request):
    # class = 'act'
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


def blogs(request):

    blogs = Blog.objects.order_by('-created_at')
    category = Category.objects.all()
    recent = Blog.objects.order_by('-created_at')[:10]

    # count categoy
    count_cate = []
    for x in blogs:
        temp = []
        for y in count_cate:
            temp.append(y['category'])
        if x.category not in temp:
            count_cate.append({
                'category': x.category,
                'count': Blog.objects.filter(category=x.category).count()
            })
    #  pagination
    per_page = 4
    list_page = []
    current_page = int(request.GET.get('page') or 1)
    max_page = math.ceil(len(blogs)/per_page)
    for i in range(0, max_page):
        list_page.append(i+1)
    result = blogs[(current_page - 1) * per_page: current_page * per_page]

    context = {
        'blogs': result,
        'category': category,
        'recent': recent,
        'count_cate': count_cate,
        'list_page': list_page,
        'current_page': current_page,
        'max_page': max_page,
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

    result = []
    blogs = Blog.objects.all()
    content = unidecode(request.GET.get('search')).split()
    category = Category.objects.all()
    recent = Blog.objects.order_by('-created_at')[:10]
    count_cate = []

    for x in blogs:
        temp = []
        for y in count_cate:
            temp.append(y['category'])
        if x.category not in temp:
            count_cate.append({
                'category': x.category,
                'count': Blog.objects.filter(category=x.category).count()
            })
    #  pagination

    for i in content:
        for x in blogs:
            if x not in result:
                if i.lower()in unidecode(x.title).lower():
                    result.append(x)
    context = {
        'blogs': result,
        'category': category,
        'recent': recent,
        'count_cate': count_cate
    }
    return render(request, 'pages/blog/listBlog.html', context)


def customHandler404(request, e):
    return render(request, 'pages/404.html')


def customHandler500(request):
    return render(request, 'pages/404.html')


def filter_category(request):
    cate = request.GET.get('category')
    # blog = Blog.objects.filter(category=cate)
    print(blogs)
    print(cate)
    # category = Category.objects.all()
    # recent = Blog.objects.order_by('-created_at')[:10]

    # # count categoy
    # count_cate = []
    # for x in blogs:
    #     temp = []
    #     for y in count_cate:
    #         temp.append(y['category'])
    #     if x.category not in temp:
    #         count_cate.append({
    #             'category': x.category,
    #             'count': Blog.objects.filter(category=x.category).count()
    #         })
    # #  pagination
    # per_page = 4
    # list_page = []
    # current_page = int(request.GET.get('page') or 1)
    # max_page = math.ceil(len(blogs)/per_page)
    # for i in range(0, max_page):
    #     list_page.append(i+1)
    # result = blogs[(current_page - 1) * per_page: current_page * per_page]

    # context = {
    #     'blogs': blogs,
    #     'category': category,
    #     'recent': recent,
    #     'count_cate': count_cate,
    #     'list_page': list_page,
    #     'current_page': current_page,
    #     'max_page': max_page,
    # }
    return render(request, 'pages/blog/listBlog.html')
