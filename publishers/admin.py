from django.contrib import admin
from .models import Publisher
# import_export
from import_export import resources
from import_export.admin import ExportActionMixin
# Register your models here.


class PublisherResource(resources.ModelResource):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'created', 'updated')


class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


admin.site.register(Publisher, PublisherAdmin)