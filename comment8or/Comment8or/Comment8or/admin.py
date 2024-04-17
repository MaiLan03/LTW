from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class CustomAdminSite(AdminSite):
    index_title = _('c8admin')
    site_header = _('c8admin')
    title_header = _('c8admin')
    logout_template = 'templates/comment8or/logged_out.html'  # Đường dẫn đến template đăng xuất tùy chỉnh

custom_admin_site = CustomAdminSite(name='custom_admin')
