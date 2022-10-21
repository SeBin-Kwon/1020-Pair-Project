from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            reviews = form.save(commit=False)
            request.user == reviews.user
            reviews.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'reviews/form.html', context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comment_form' : comment_form,
        'comments' : review.comment_set.order_by('-pk'),
    }
    return render(request, 'reviews/detail.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('reviews:index')

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            reviews = form.save(commit=False)
            request.user == reviews.user
            reviews.save()
            return redirect('reviews:detail', pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form' : form
    }
    return render(request, 'reviews/form.html', context)

def comments(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            request.user == comment.user
            comment.save()
    return redirect('reviews:detail', review.pk)