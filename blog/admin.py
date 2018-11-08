from django.contrib import admin

# Register your models here.

from .models import BlogArticle
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    list_filter = ("publish","author")
    search_fields = ("title","body")

    date_hierarchy = "publish"
    ordering = ['-publish',]

admin.site.register(BlogArticle,BlogArticleAdmin)
