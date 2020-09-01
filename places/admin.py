from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 3  # even without it there is no position numbers displayed
    readonly_fields = ('preview_img',)
    fields = ('image', 'preview_img')

    def preview_img(self, obj):
        return format_html(
            '<img style="max-width: 200px; height: auto;" src="{}" width="{}" height={} />',
            obj.image.url,
            obj.image.width,
            obj.image.height,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
