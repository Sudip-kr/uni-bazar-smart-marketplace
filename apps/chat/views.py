from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from apps.listings.models import Item
from .models import ChatRoom


# =========================
# START CHAT
# =========================
@login_required
def start_chat(request, item_id):

    item = get_object_or_404(Item, id=item_id)

    # Prevent seller chatting with self
    if request.user == item.seller:
        return redirect('listings:item_detail', item.id)

    # Create room if not exists
    room, created = ChatRoom.objects.get_or_create(
        item=item,
        buyer=request.user,
        seller=item.seller
    )

    return redirect('chat:chat_room', room.id)


# =========================
# CHAT ROOM
# =========================
@login_required
def chat_room(request, room_id):

    room = get_object_or_404(ChatRoom, id=room_id)

    # SECURITY CHECK
    if request.user != room.buyer and request.user != room.seller:
        return redirect('core:home')

    # MARK AS READ
    room.messages.exclude(
        sender=request.user
    ).update(is_read=True)

    # CURRENT ROOM MESSAGES
    messages = room.messages.all().order_by('timestamp')

    # ALL USER ROOMS
    rooms = ChatRoom.objects.filter(
        Q(buyer=request.user) |
        Q(seller=request.user)
    ).distinct().order_by('-created_at')

    return render(request, 'chat/chat_room.html', {
        'room': room,
        'messages': messages,
        'rooms': rooms
    })

# =========================
# INBOX
# =========================
@login_required
def inbox(request):

    rooms = ChatRoom.objects.filter(
        Q(buyer=request.user) |
        Q(seller=request.user)
    ).distinct().order_by('-created_at')

    room_data = []

    for room in rooms:

        last_message = room.messages.order_by('-timestamp').first()

        unread_count = room.messages.exclude(
            sender=request.user
        ).filter(
            is_read=False
        ).count()

        room_data.append({
            'room': room,
            'last_message': last_message,
            'unread_count': unread_count,
        })

    return render(request, 'chat/inbox.html', {
        'room_data': room_data
    })