from django.shortcuts import render, redirect, get_object_or_404
from .models import Model_for_tracks, Pictures_for_track

def track_index(request):
    all_tracks = Model_for_tracks.objects.all()
    context = {
        'all_tracks': all_tracks,
    }
    return render(request, 'track_map/track_index.html', context)