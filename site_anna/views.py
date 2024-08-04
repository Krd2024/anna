from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import PdfModel, PhotoReview, Results, Review, User
from site_anna.forms import ReviewForm

from django.shortcuts import render, redirect
from .email.send_mail import send_mail_

from .forms import ReviewForm


# def flag_user(request):
#     if request.user.is_authenticated:
#         try:
#             user = User.objects.get(pk=request.user.id)
#             flag = 1 if user.on_the_list else 0
#         except Exception as e:
#             print(e)
#     else:
#         flag = 0
#     return flag


def index(request):

    # return render(request, "index.html", {"flag": flag_user(request)})
    return render(request, "index.html")


def about_me(request):
    # return render(request, "about_me.html", {"flag": flag_user(request)})
    return render(request, "about_me.html")


def results(request):
    results = Results.objects.all()
    return render(
        # request, "results.html", {"flag": flag_user(request), "results": results}
        request,
        "results.html",
        {"results": results},
    )


def contact(request):
    return render(request, "contact.html")
    # return render(request, "contact.html", {"flag": flag_user(request)})


def education(request):
    return render(request, "education.html")
    # return render(request, "education.html", {"flag": flag_user(request)})


def price(request):
    # return render(request, "price.html", {"flag": flag_user(request)})
    return render(request, "price.html")


def materials(request):
    return render(request, "materials.html")


# def materials1(request):
#     return HttpResponse('<script>window.open("/materials/");</script>')


def faq(request):
    return render(request, "faq.html")
    # return render(request, "faq.html", {"flag": flag_user(request)})


def review(request):
    """Отзывы"""

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            if form.cleaned_data["rating"] is not None:
                rating = form.cleaned_data["rating"]
            else:
                rating = ""
            if form.cleaned_data["text"] is not None:
                text = form.cleaned_data["text"]
            else:
                text = ""

            # print(form.cleaned_data["text"], "<<< ---------- text")
            # print(form.cleaned_data["rating"], "<<< ---------- rating")
            message = f"Отзыв: {text}\nРейтинг: {rating}"
            send_mail_(message)
            # send_mail_("polzovatel.krasnodar@bk.ru", message)

            return redirect("review")

        return redirect("review")  # or whatever URL you want to redirect to
    else:

        form = ReviewForm()
        reviews = Review.objects.all()
        context = {"reviews": reviews, "form": form}
        # context = {"reviews": reviews, "form": form, "flag": flag_user(request)}
        return render(request, "review.html", context)


def pdf_list(request):
    pdf_list = PdfModel.objects.all()

    return render(
        request,
        "pdf_list.html",
        {"pdf_list": pdf_list},
        # request, "pdf_list.html", {"pdf_list": pdf_list, "flag": flag_user(request)}
    )


def education_photo(request):
    education_photo = PhotoReview.objects.all()
    return render(
        request,
        "education_photo2.html",
        {
            "education_photo": education_photo,
            # "flag": flag_user(request),
            "slide_count": len(education_photo),
        },
    )


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
