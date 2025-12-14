from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review

def reviews_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

@login_required
def review_add(request):
    if request.method == 'POST':
        Review.objects.create(
            user=request.user,
            rating=int(request.POST.get('rating')),
            comment=request.POST.get('comment')
        )
        return redirect('reviews')

    return render(request, 'reviews/review_add.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review.rating = request.POST.get('rating')
        review.comment = request.POST.get('comment')
        review.save()
        return redirect('reviews')

    return render(request, 'reviews/edit_review.html', {'review': review})