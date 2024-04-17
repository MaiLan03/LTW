from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review, ContributorAdmin)
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)

admin.site.unregister(Contributor)
admin.site.register(Contributor, ContributorAdmin)



from django.contrib.admin import AdminSite
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)
class BookrAdminSite(AdminSite):
 title_header = 'Bookr Admin'
 site_header = 'Bookr administration'
 index_title = 'Bookr site admin'
admin_site = BookrAdminSite(name='bookr')
# Register your models here.
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)
#
#
class BookAdmin(admin.ModelAdmin):
 list_display = ('title', 'isbn')
admin.site.unregister(Book)
admin.site.register(Book, BookAdmin)