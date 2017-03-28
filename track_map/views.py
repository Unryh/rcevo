from django.shortcuts import render, redirect, get_object_or_404
from .models import Track, PictureForTrack

def track_index(request):
    all_tracks = Track.objects.all()
    context = {
        'all_tracks': all_tracks,
    }
    return render(request, 'track_map/track_index.html', context)