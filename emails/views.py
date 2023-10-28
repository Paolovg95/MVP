from django.shortcuts import render
from .models import EmailEntry
from django.http import HttpResponse, Http404
# Create your views here.

#html_str = "<!doctype html><html><body><h1>{email}</h1></body></html>"

def email_entry_get_view(request, id=id, *args, **kwargs):
    print(args,kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
        #my_html = html_str.format(email=obj.email)
    except EmailEntry.DoesNotExist:
        raise Http404
    return render(request, "get.html", {"obj": obj})
