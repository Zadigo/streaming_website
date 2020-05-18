from django import http
from django.shortcuts import get_object_or_404, render, redirect
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
        name = request.POST['name']
        stream = get_object_or_404(models.Stream, key=name)

        # Ban streamers by setting them inactive
        # if not stream.user.is_active:
        #     return HttpResponseForbidden("Inactive user")

        # Don't allow the same stream to be published multiple times
        # if stream.started_at:
        #     return HttpResponseForbidden("Already streaming")

        stream.started_at = timezone.now()
        stream.save()

        # Redirect to the streamer's public username
        return redirect(stream.user.username)

@method_decorator(csrf_exempt, 'dispatch')
class StopStream(View):
    """ This view is called when a stream stops
    """
    def post(self, request, **kwargs):
        name = request.POST["name"]
        models.Stream.objects.filter(key=name).update(started_at=None)
        return http.HttpResponse('OK')

def fake_view(*args, **kwargs):
    """ This view should never be called because the URL paths
        that map here will be served by nginx directly.
    """
    raise Exception('This should never be called!')