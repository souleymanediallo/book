from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

site_header = 'Bookstore Admin'
site_title = 'Bookstore Admin Portal'
index_title = 'Welcome to Bookstore Admin Portal'
admin.site.site_header = site_header
admin.site.site_title = site_title
admin.site.index_title = index_title
