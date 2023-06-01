from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at') # this is the list of fields that will be displayed in the admin page

admin.site.register(Note, NoteAdmin)