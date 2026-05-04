from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.listings.models import Item
from .models import Feedback


# =========================
# HOME PAGE
# =========================
def home(request):

    latest_items = Item.objects.filter(
        status='available'
    ).order_by('-created_at')[:8]

    return render(request, 'core/home.html', {
        'latest_items': latest_items
    })


# =========================
# FEEDBACK PAGE
# =========================
@login_required
def feedback_page(request):

    if request.method == 'POST':

        comment = request.POST.get('comment')

        # 500 WORD LIMIT CHECK
        if comment and len(comment) <= 500:

            Feedback.objects.create(
                user=request.user,
                comment=comment
            )

            return redirect('core:feedback')

    feedbacks = Feedback.objects.all().order_by('-created_at')

    return render(request, 'core/feedback.html', {
        'feedbacks': feedbacks
    })