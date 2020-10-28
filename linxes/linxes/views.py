import secrets
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib import messages
from django.db.models import Q
from . import models
from . import forms


class HomeLink(FormView):
    """HomeLink - view class for link home form page"""
    model_class = models.Link
    form_class = forms.LinkForm
    template_name = r"base.html"

    def get(self, request, short_link='', *args, **kwargs):
        """home - show home page"""
        if short_link:
            link = get_object_or_404(self.model_class, short_link=short_link)
            link.link_redirects += 1
            path = str(link.long_link)
            link.save()
            return redirect(to=path)
        else:
            form = self.form_class()
            return render(
                request=request,
                template_name='base.html',
                context={
                    'form': form,
                }
            )

    def post(self, request, short_link='', *args, **kwargs):
        sl = None
        lnk = request.POST['long_link']
        links = models.Link.objects.filter(Q(short_link__exact=lnk) | Q(long_link__exact=lnk))
        if len(links):
            messages.add_message(
                request,
                messages.SUCCESS,
                _('Link "%s" Status') % (links[0].short_link,)
            )
            return render(
                request,
                self.template_name,
                {
                    'links': {
                        'long_link': links[0].long_link,
                        'short_link': links[0].short_link,
                        'link_redirects': links[0].link_redirects,
                    },
                },
            )
        else:
            link = self.model_class()
            form = self.form_class(
                request.POST or None,
                instance=link
            )
            if form.is_valid():
                do = True
                while do:
                    sl = secrets.token_urlsafe(nbytes=5)
                    do = (len(models.Link.objects.filter(short_link__exact=lnk)) != 0)
                link.long_link = lnk
                link.short_link = sl
                link.link_redirects = 0
                link.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    _('Link Data is saved. Short link: %s') % (sl, )
                )
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    _('Link Data is not saved')
                    )
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'links': links,
                'short_link': sl,
            },
        )
