from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == "POST":
        img = request.POST.get("image")
        print(img)
        return HttpResponse("index.html", {
            "image": img,
            })
    return render(request, 'index.html', {})
