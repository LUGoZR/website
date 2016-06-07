from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from .models import News, Event, Participant
from .forms import Subscribe


def homepage(request):
    if request.method == "POST":
        form = Subscribe(request.POST)
        if form.is_valid():
            form.save()
            response = TemplateResponse(request, "homepage.html", {"vesti": News.objects.all(), "form": form})
        else:
            response = TemplateResponse(request, "homepage.html", {"vesti": News.objects.all(), "form": form})
    else:
        form = Subscribe()
        response = TemplateResponse(request, "homepage.html", {"vesti": News.objects.all(), "form": form})

    return response


def blog(request):
    return TemplateResponse(request, "blog.html", {"items": News.objects.all()})


def blog_post(request, blog_id):
    blog = get_object_or_404(News, pk=blog_id)
    return TemplateResponse(request, "blog_post.html", {"item": blog})


def news_post(request, news_id):
    blog = get_object_or_404(News, pk=news_id)
    return TemplateResponse(request, "blog_post.html", {"item": blog})


def events(request):
    return TemplateResponse(request, "events.html", {"items": Event.objects.all()})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants_count = Participant.objects.filter(event=event).count()
    return TemplateResponse(request, "event_detail.html", {"item": event, "count": participants_count})


def event_join(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participants_count = Participant.objects.filter(event=event).count()
    return TemplateResponse(request, "event_detail.html", {"item": event, "count": participants_count})
