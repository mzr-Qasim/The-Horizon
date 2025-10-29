from django.shortcuts import render





def all_rooms(request):
    return render(request, 'rooms/rooms.html')