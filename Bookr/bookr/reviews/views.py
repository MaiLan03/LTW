# from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
#
# def base1(request):
#  return render(request, "base1.html")
#
# def c1bai1(request):
#  return render(request, "C1bai1.html")
# def c1bai2(request):
#  search = request.GET.get("search")
#  return render(request,"C1bai2.html",{"search":format(search)})
#
# from django.http import HttpResponse
# from .models import Book
# def welcome_view(request):
#  message = f"<html><h1>Welcome to Bookr!</h1><p>{Book.objects.count()} books and counting!</p></html>"
#  return HttpResponse(message)
#
# from django.shortcuts import render
# def welcome_view (request):
#  return render(request, 'base.html')
#
# from django.shortcuts import render, get_object_or_404
# from .models import Book
# from .utils import average_rating
# def index(request):
#  return render(request, "base.html")
# def book_search(request):
#  search_text = request.GET.get("search", "")
#  return render(request,"reviews/search-results.html",{"search_text": search_text})

# -----------------------------
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import SearchForm, ReviewForm
from .utils import average_rating
from .forms import PublisherForm
from django.shortcuts import get_object_or_404, redirect
from .models import Book, Contributor, Publisher, Review
from django.contrib import messages



def welcome_view (request):
 return render(request, 'base.html')


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(
                first_names__icontains=search
            )

            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = Contributor.objects.filter(
                last_names__icontains=search
            )

            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

    return render(
        request,
        "reviews/search-results.html",
        {"form": form, "search_text": search_text, "books": books},
    )


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append(
            {
                "book": book,
                "book_rating": book_rating,
                "number_of_reviews": number_of_reviews,
            }
        )

    context = {"book_list": book_list}
    return render(request, "reviews/book_list.html", context)

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {"book": book, "book_rating": book_rating, "reviews": reviews}
    else:
        context = {"book": book, "book_rating": None, "reviews": None}
    return render(request, "reviews/book_detail.html", context)

# ------------------

def publisher_edit(request, pk=None):
 if pk is not None:
    publisher = get_object_or_404(Publisher, pk=pk)
 else:
    publisher = None
 if request.method == "POST":
     form = PublisherForm(request.POST, instance=publisher)
     if form.is_valid():
        updated_publisher = form.save()
        if publisher is None:
            messages.success(request, f"Publisher {updated_publisher} was created.")
        else:
            messages.success(request, f"Publisher {updated_publisher} was updated.")
        return redirect("publisher_edit", pk=updated_publisher.pk)
 else:
     form = PublisherForm(instance=publisher)
 return render(request, "instance-form.html",
               {"method": request.method, "form": form, "model_type": "Publisher", "instance": publisher})


# ----

def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                messages.success(request, 'Review for "{}" created.'.format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, 'Review for "{}" updated.'.format(book))

            updated_review.save()
            return redirect("book_detail", book.pk)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "instance-form.html",
        {
            "form": form,
            "instance": review,
            "model_type": "Review",
            "related_instance": book,
            "related_model_type": "Book",
        },
    )


