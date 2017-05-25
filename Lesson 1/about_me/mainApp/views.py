from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'index.html')


def works_page(request):
    return render(request, 'works.html')


def learns_page(request):
    return render(request, 'learns.html')
