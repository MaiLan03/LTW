from django.contrib.admin.apps import AdminConfig
from django.contrib import admin

class ReviewsAdminConfig(AdminConfig):
    default_site = 'admin.BookrAdminSite'
