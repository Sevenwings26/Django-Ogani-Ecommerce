from django.shortcuts import render, redirect


# main pages 
def index(request):
    return render(request, "pages/index.html", )

def shop(request):
    return render(request, "pages/shop.html", )

def blog(request):
    return render(request, "pages/blog.html", )

def contact(request):
    return render(request, "pages/contact.html", )

