from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from .models import Quotation, Category, Project, Contact, ClientReview, Service
# Create your views here.


def index(request):
    work = Project.objects.all().order_by("-date_posted")
    reviews = ClientReview.objects.all().order_by("-review_date")
    contactUs = Contact.objects.all()

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        comapany = request.POST["comapany"]
        message = request.POST["message"]

        contact = Contact(name=name)
        contact.email = email
        contact.phone = phone
        contact.comapany = comapany
        contact.message = message

        contact.save()
        messages.success(
            request, "Your Message Has Been Sent Successfully.")
        return redirect("/")

    context = {
        "work": work,
        "contactUs": contactUs,
        "reviews": reviews
    }

    return render(request, "codezyners/index.html", context)


def about(request):
    return render(request, "codezyners/about.html")


def reviews(request):
    client_reviews = ClientReview.objects.all().order_by("-review_date")

    context = {
        "client_reviews": client_reviews
    }
    return render(request, "codezyners/client_reviews.html", context)


def addReview(request):
    reviewServices = Service.objects.all()
    if request.method == "POST":
        client_name = request.POST["client_name"]
        client_email = request.POST["client_email"]
        client_business = request.POST["client_business"]
        client_services = request.POST["client_services"]
        client_review = request.POST["client_review"]

        newReview = ClientReview(client_name=client_name)
        newReview.client_email = client_email
        newReview.client_business = client_business
        newReview.client_services = client_services
        newReview.client_review = client_review

        newReview.save()
        messages.success(
            request, "Your Review Has Been Posted Successfully.")
        return redirect("reviews")

    context = {"reviewServices": reviewServices}

    return render(request, "codezyners/reviewForm.html", context)


def ourProjects(request, *args, **kwargs):
    categories = Category.objects.all()

    # Filter by Category
    category = request.GET.get('category')
    if category:
        projects = Project.objects.order_by(
            '-date_posted').filter(category__category_name=category)
    else:
        projects = Project.objects.all()

    # Pagination
    pagination = Paginator(projects, 20)
    current_page = request.GET.get('page')

    try:
        pageList = pagination.get_page(current_page)
    except PageNotAnInteger:
        pageList = pagination.page(1)
    except (EmptyPage, InvalidPage):
        pageList = pagination.page(pagination.num_pages)

    context = {
        "projects": projects,
        "pageList": pageList,
        "categories": categories,
    }

    return render(request, "codezyners/ourWork.html", context)


def quota(request):
    ourServices = Service.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        service = request.POST['service']
        service_desc = request.POST['service_desc']
        approxBudget = request.POST['approxBudget']

        quota = Quotation(name=name)
        quota.phone = phone
        quota.email = email
        quota.service = service
        quota.service_desc = service_desc
        quota.approxBudget = approxBudget

        quota.save()
        messages.success(
            request, "Your Quotation Has Been Submitted Successfully.")
        return redirect("quota")

    context = {"ourServices": ourServices}
    return render(request, "codezyners/quota.html", context)
