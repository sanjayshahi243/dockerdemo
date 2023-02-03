from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from demoApp.models import AppModel
from django.contrib import messages
from django.conf import settings

# Create your views here.


def error_404(request, exception):
    return render(request, "errorPages/404.html", status=404)


def error_500(request):
    return render(request, "errorPages/500.html")


def index_view(request):
    return render(request, "index.html")


def raise_401(request):
    return HttpResponse(request, status=401)


def raise_500(request):
    raise SyntaxError


def add_files(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        title = request.POST.get("title")
        message = request.POST.get("message")

        with open("{}/{}.txt".format(settings.MEDIA_ROOT, fname), "w") as f:
            f.write(message)

        AppModel.objects.create(title=title, message=message)
        messages.add_message(request, messages.SUCCESS, "Successfully created.")

        return redirect(reverse_lazy("list_file"))

    else:
        return render(request, "demoApp/form.html")


def list_files(request):
    file_list = AppModel.objects.all()
    context = {
        "file_list": file_list,
    }
    return render(request, "demoApp/list.html", context=context)
