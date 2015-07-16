#-*- coding: utf-8 -*-
from django.db import models

class Song_list(models.Model):
    class Meta(object):
        verbose_name = u'Пісня'
        verbose_name_plural = u'Пісні'

    artist_name = models.CharField(max_length=7, blank=False, verbose_name=u"Виконавець")
    composition_name = models.CharField(max_length=7, blank=False, verbose_name=u"Пісня")

    def __unicode__(self):
        return u"%s %s" % (self.artist_name, self.composition_name)

