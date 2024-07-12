from django.http import HttpResponse
from django.shortcuts import redirect, render

from site_anna.forms import ReviewForm


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


def create_review(request, product_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.save()
            return redirect("product_detail", product_id=product_id)
    else:
        form = ReviewForm()
    return render(request, "reviews/create_review.html", {"form": form})
