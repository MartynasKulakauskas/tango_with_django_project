from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    return render(request, 'rango/index.html', context=context_dict)
    
    
    

def about(request):
    
    context_dicti = {'boldmessage': 'This tutorial has been put together by Martynas'}
    
    return render(request, 'rango/index.html', context=context_dicti)