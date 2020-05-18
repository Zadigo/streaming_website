from django import http
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView

from streamer import models

class HomePage(TemplateView):
    template_name = 'pages/stream.html'

@method_decorator(csrf_exempt, 'dispatch')
class StartStream(View):
    """ This view is called to start the stream
    """
    def post(self, request, **kwargs):
        try:
            key = request.POST['key']
        except:
            return http.HttpResponseForbidden()
        else:
            stream = get_object_or_404(models.Stream, key=key)

        # Ban streamers by setting them inactive
        if not stream.user.is_active:
            return http.JsonResponse(data={'state': 'forbidden'})

        # Don't allow the same stream to be published multiple times
        if stream.started_on:
            return http.JsonResponse(data={'activity': True})

        stream.started_on = timezone.now()
        stream.save()
        return http.JsonResponse(data={'redirect_to': reverse('current_steam_url', args=[stream.user.username])})

@method_decorator(csrf_exempt, 'dispatch')
class StopStream(View):
    """ This view is called when a stream stops
    """
    def post(self, request, **kwargs):
        key = request.POST['key']
        models.Stream.objects.filter(key=key).update(started_on=None)
        return http.JsonResponse(data={'activity': False})

def fake_view(*args, **kwargs):
    """ This view should never be called because the URL paths
        that map here will be served by nginx directly.
    """
    print(args, kwargs)
    raise Exception('This should never be called!')
