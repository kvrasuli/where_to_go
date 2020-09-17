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
        try:
            return format_html(
                '<img style="max-width: 200px;" src="{}"/>',
                obj.image.url,
            )
        except ValueError:
            return format_html('<p>Preview is not available by now.</p>')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
