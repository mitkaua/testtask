#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song/base.html', {'songs': songs})