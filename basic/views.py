from django.shortcuts import render

# Create your views here.
def index(request):
    temp = [1,2,4,5,6,7,8,9]
    return render(request, 'main.html', {"temp":temp})