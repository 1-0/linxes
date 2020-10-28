from django.db import models
from django.utils.translation import gettext as _


class Link(models.Model):
    """Link - class for link content"""

    long_link = models.CharField(_('Long Link'), max_length=1023, unique=True)
    short_link = models.CharField(_('Short Link'), max_length=255, unique=True)
    link_redirects = models.PositiveIntegerField(_('Count Link Redirects'))
    pub_date = models.DateField(_('Link Date Published'), auto_now=True)

    readonly_fields = ('pub_date',)
    ordering = ['-pub_date', '-id', 'title']

    def __repr__(self):
        return _("<Link #%s") % (self.id, )

    def __str__(self):
        return _("<Link #%s") % (self.id, )
