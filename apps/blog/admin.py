from django.contrib import admin
from .models import Post, Comment


# Action
def approve_comments(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_comments.short_description = "Approve selected comments"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    actions = [approve_comments]

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)