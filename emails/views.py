from django.shortcuts import render
from .models import EmailEntry
from django.http import HttpResponse, Http404
# Create your views here.

def email_entry_get_view(request, id=id, *args, **kwargs):
    print(args,kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    return HttpResponse(f"<h1> Hello {obj.email}</h1>")
