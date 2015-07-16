#-*- coding: utf-8 -*-
from django.db import models

class Song(models.Model):
    class Meta(object):
        verbose_name = u'Пісня'
        verbose_name_plural = u'Пісні'

    artist_name = models.CharField(max_length=250, blank=False, verbose_name=u"Виконавець")
    composition_name = models.CharField(max_length=250, blank=False, verbose_name=u"Пісня")
    photo = models.ImageField(blank=True, verbose_name=u'Фото', null=True)

    def __unicode__(self):
        return u"%s %s" % (self.artist_name, self.composition_name)

