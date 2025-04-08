from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'comedy_text')  # show in list view
    list_filter = ('is_done',)  # filter sidebar
    search_fields = ('title', 'description', 'comedy_text')  # search box
