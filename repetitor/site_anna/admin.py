from django.contrib import admin

# myapp/admin.py
from django.contrib import admin
from .models import StudentAchievement, User, Review, PdfModel


class Model_user_admin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")
    search_fields = ("username",)


class Model_review_admin(admin.ModelAdmin):
    list_display = ("user", "text", "created_at", "rating")
    search_fields = ("username",)


class Model_pdf_admin(admin.ModelAdmin):
    list_display = ("name", "pdf_file", "created_at")
    fields = ("name", "pdf_file")


class Model_atudentAchievement_admin(admin.ModelAdmin):
    list_display = ("name", "text", "created_at")
    fields = ("name", "pdf_file")
    search_fields = ("username",)


admin.site.register(PdfModel, Model_pdf_admin)
admin.site.register(User, Model_user_admin)
admin.site.register(Review, Model_review_admin)
admin.site.register(StudentAchievement, Model_atudentAchievement_admin)
