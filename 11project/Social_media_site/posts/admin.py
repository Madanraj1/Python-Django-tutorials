from django.contrib import admin
from .models import Post, Comment, Profile



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created','active')
    list_filter = ('active','created')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'photo']