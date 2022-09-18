from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main_view(request):
    if request.method == "GET":
        context = {'data': 'username'}
        return render(request, 'chat_index.html', context=context)
    
    elif request.method == "POST":
        print(request.POST)
        return HttpResponse('OK!')
