"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# import reviews.views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', reviews.views.base1),
#     path('c1bai1',reviews.views.c1bai1),
#     path('bookr-search', reviews.views.c1bai2)
# ]
#
# from django.contrib import admin
# from django.urls import include, path
# import reviews.views
# urlpatterns = [
#  path('admin/', admin.site.urls),
#  path("book-search", reviews.views.book_search),
#  path('', include('reviews.urls'))
# ]

from reviews.admin import admin_site
import reviews.views
from django.urls import include, path
urlpatterns = [
 path("admin/", admin_site.urls),
 path("book-search/", reviews.views.book_search, name="book_search"),
 path("", include("reviews.urls")),
]