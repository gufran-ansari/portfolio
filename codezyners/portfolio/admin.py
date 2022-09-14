from django.contrib import admin
from .models import Quotation, Project, Category, Contact, ClientReview, Service

# Register your models here.
admin.site.register(Quotation)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(ClientReview)
admin.site.register(Service)
