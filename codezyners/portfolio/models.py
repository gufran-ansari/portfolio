from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

CATEGORIES = [
    ("Graphic Design", "design"),
    ("Web Development", "web-dev"),
]

SERVICES = [
    ("Logo", "Logo"),
    ("Flyer", "Flyer"),
    ("Broucher", "Broucher"),
    ("Templates", "Templates"),
    ("Web Design", "Web Design"),
    ("Print Design", "Print Design"),
    ("Visiting Card", "Visiting Card"),
    ("Website Development", "Website Development"),
]


class Category(models.Model):
    category_name = models.CharField(max_length=255, choices=CATEGORIES)

    def __str__(self):
        return f"{self.pk}. {self.category_name}"


class Service(models.Model):
    service_name = models.CharField(max_length=255, choices=SERVICES)

    def __str__(self):
        return f"{self.pk}. {self.service_name}"


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True)
    client_email = models.EmailField(max_length=255, blank=True)
    client_business = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    projectImage = models.ImageField(upload_to='image/our_work')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_name} is uploaded by {str(self.user)}"

    @staticmethod
    def posts_by_id(category_id):
        if category_id:
            return Project.objects.filter(category=category_id)
        else:
            return Project.objects.all()

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})


class ClientReview(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    client_business = models.CharField(max_length=255)
    client_services = models.CharField(max_length=255, choices=SERVICES)
    client_review = models.TextField()
    review_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review from {self.client_name}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    comapany = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.timestamp}"
