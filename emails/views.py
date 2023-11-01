from django.shortcuts import render
from .models import EmailEntry
from django.http import HttpResponse, Http404
from .forms import EmailEntryForm

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


def email_entry_create_view(request, *args, **kwargs):
    print(request.user,request.user.is_authenticated)

    form = EmailEntryForm(request.POST)
    if request.method == 'POST':
        #print(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.name = "N/A"
            # obj.save()
            #print(form.clean_email())
            form.save()

            form = EmailEntryForm()

    return render(request, "form.html", {'form': form})
