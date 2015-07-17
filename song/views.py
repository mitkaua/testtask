#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Song

def song_list(request):
    songs = Song.objects.all()
    songs = songs.order_by('artist_name')
    if request.GET.get('order_by', '') == '':
        request.GET.order_by = 'artist_name'
    order_by = request.GET.get('order_by', '')
    if order_by in ('artist_name', 'composition_name', 'id'):
        songs = songs.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            songs = songs.reverse()
    return render(request, 'song/base.html', {'songs': songs})