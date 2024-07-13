from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import PdfModel, PhotoReview, Review
from site_anna.forms import ReviewForm

from django.shortcuts import render, redirect

from .forms import ReviewForm


def index(request):

    return render(request, "main.html")


def index_ege(request):
    return render(request, "ege.html")


def about_me(request):
    return render(request, "about_me.html")


def advantages(request):
    return render(request, "advantages.html")


def contact(request):
    return render(request, "contact.html")


def education(request):
    return render(request, "education.html")


def price(request):
    return render(request, "price.html")


def materials(request):
    return render(request, "materials.html")


def materials1(request):
    return HttpResponse('<script>window.open("/materials/");</script>')


def faq(request):
    return render(request, "faq.html")


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("review")  # or whatever URL you want to redirect to
    else:
        # form = ReviewForm()
        # return render(request, "test.html", {"form": form})
        form = ReviewForm()
        reviews = Review.objects.all()
        context = {"reviews": reviews, "form": form}
    return render(request, "review.html", context)


def pdf_list(request):
    pdf_list = PdfModel.objects.all()
    print("PDF")

    return render(request, "pdf_list.html", {"pdf_list": pdf_list})


def education_photo(request):
    education_photo = PhotoReview.objects.all()
    return render(request, "education_photo.html", {"education_photo": education_photo})


# def create_review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.save()
#             return redirect("review_list")  # or whatever URL you want to redirect to
#     else:
#         form = ReviewForm()
#     return render(request, "test.html", {"form": form})
#     # return render(request, "create_review.html", {"form": form})
