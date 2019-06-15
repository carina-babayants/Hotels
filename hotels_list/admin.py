from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from hotels_list.models import Hotel, Comments


class HotelAdmin(SummernoteModelAdmin):
    summer_note_fields = ('hotel', 'address', 'description', 'capacity', 'type', 'facilities', 'owner',)

admin.site.register(Hotel, HotelAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'created', 'moderation')
admin.site.register(Comments, CommentAdmin)



