from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import EmailEntry
from django.http import HttpResponse, Http404
from .forms import EmailEntryForm, EmailEntryUpdateForm

# Create your views here.

#html_str = "<!doctype html><html><body><h1>{email}</h1></body></html>"

@login_required(login_url="/login")
def email_entry_get_view(request, id=id, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
        #my_html = html_str.format(email=obj.email)
    except EmailEntry.DoesNotExist:
        raise Http404
    return render(request, "get.html", {"obj": obj})


def email_entry_create_view(request, *args, **kwargs):
    # print(request.user,request.user.is_authenticated)

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

@login_required(login_url="/login")
def email_entry_destroy_view(request, id=id, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
        #my_html = html_str.format(email=obj.email)
        if request.method == "POST":
            obj.delete()
            return redirect("/")
    except EmailEntry.DoesNotExist:
        raise Http404


    return render(request, "emails/destroy.html", {"obj": obj})


@login_required(login_url="/login")
def email_entry_list_view(request,*args, **kwargs):
    obj = EmailEntry.objects.all()


    return render(request, "emails/list.html", {"object_list": obj})



def email_entry_update_view(request, id=id, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except:
        raise Http404

    form =  EmailEntryUpdateForm(request.POST, instance=obj)
    if form.is_valid():
        updated_obj = form.save()
        return redirect(f"/email/{updated_obj.id}")

    return render(request, "emails/update.html", {'object': obj,'form': form})
