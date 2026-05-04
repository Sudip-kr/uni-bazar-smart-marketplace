from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item
from .forms import ItemForm
from django.db.models import Q

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user

            if item.location_type == 'day_scholar':
                item.hostel_name = ''

            item.save()
            messages.success(request, 'Item listed successfully!')
            return redirect('listings:my_items')
    else:
        form = ItemForm()

    return render(request, 'listings/item_create.html', {'form': form})

@login_required
def my_items(request):
    items = Item.objects.filter(seller=request.user).order_by('-created_at')
    return render(request, 'listings/my_items.html', {'items': items})


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, seller=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            updated_item = form.save(commit=False)

            if updated_item.location_type == 'day_scholar':
                updated_item.hostel_name = ''

            updated_item.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('listings:my_items')
    else:
        form = ItemForm(instance=item)

    return render(request, 'listings/item_edit.html', {'form': form, 'item': item})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, seller=request.user)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('listings:my_items')

    return render(request, 'listings/item_delete.html', {'item': item})


@login_required
def mark_as_sold(request, pk):
    item = get_object_or_404(Item, pk=pk, seller=request.user)
    item.status = 'sold'
    item.save()
    messages.success(request, 'Item marked as sold!')
    return redirect('listings:my_items')

def item_list(request):
    items = Item.objects.filter(status='available').order_by('-created_at')

    query = request.GET.get('q')
    category = request.GET.get('category')
    condition = request.GET.get('condition')
    location_type = request.GET.get('location_type')
    sort = request.GET.get('sort')

    # Search
    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # Filters
    if category:
        items = items.filter(category=category)

    if condition:
        items = items.filter(condition=condition)

    if location_type:
        items = items.filter(location_type=location_type)

    # Sorting
    if sort == 'price_low':
        items = items.order_by('price')
    elif sort == 'price_high':
        items = items.order_by('-price')
    else:
        items = items.order_by('-created_at')

    context = {
        'items': items,
        'query': query,
        'selected_category': category,
        'selected_condition': condition,
        'selected_location_type': location_type,
        'selected_sort': sort,
        'category_choices': Item.CATEGORY_CHOICES,
        'condition_choices': Item.CONDITION_CHOICES,
        'location_choices': Item.LOCATION_TYPE_CHOICES,
    }

    return render(request, 'listings/item_list.html', context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'listings/item_detail.html', {'item': item})

@login_required
def toggle_wishlist(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.user in item.wishlist.all():
        item.wishlist.remove(request.user)
        messages.info(request, 'Item removed from wishlist.')
    else:
        item.wishlist.add(request.user)
        messages.success(request, 'Item added to wishlist.')

    return redirect(request.META.get('HTTP_REFERER', 'listings:item_list'))    

@login_required
def wishlist_items(request):
    items = request.user.wishlist_items.all()

    return render(request, 'listings/wishlist.html', {
        'items': items
    })