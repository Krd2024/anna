from django.contrib import admin

from .models import PhotoReview, Results, StudentAchievement, User, Review, PdfModel
from django.contrib.auth.admin import UserAdmin


class Model_user_admin(UserAdmin):

    list_display = ("username", "email", "phone_number", "on_the_list")
    search_fields = ("username",)
    list_editable = ("on_the_list", "phone_number")

    # def get_list_display(self, request):
    #     return ["username", "email", "phone_number", "on_the_list"]


class Model_review_admin(admin.ModelAdmin):
    list_display = ("user", "text", "created_at", "rating")
    search_fields = ("username",)
    list_editable = ("text", "rating")


class Model_pdf_admin(admin.ModelAdmin):
    list_display = ("name", "pdf_file", "created_at")
    fields = ("name", "pdf_file")


class Model_atudentAchievement_admin(admin.ModelAdmin):
    list_display = ("name", "text", "created_at")
    fields = ("name", "pdf_file")
    search_fields = ("username",)


class Model_PhotoReview_admin(admin.ModelAdmin):
    list_display = ("image", "created_at")


class Model_resusultsPdf_admin(admin.ModelAdmin):
    list_display = ("name", "pdf_file_results", "created_at")
    search_fields = ("name",)


admin.site.register(User, Model_user_admin)
admin.site.register(PdfModel, Model_pdf_admin)
admin.site.register(Review, Model_review_admin)
admin.site.register(StudentAchievement, Model_atudentAchievement_admin)
admin.site.register(PhotoReview, Model_PhotoReview_admin)
admin.site.register(Results, Model_resusultsPdf_admin)
