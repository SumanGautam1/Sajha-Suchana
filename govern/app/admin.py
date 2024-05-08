from django.contrib import admin
from .models import Heading,Feedback,Government

# Register your models here.
@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    list_display = ['id','title','image','desc']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','desc','image']

@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','about','source']