from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request, 'mainapp/homePage.html')

def contact (request):
    return render(request, 'mainapp/basic.html', {'values':['Если есть вопросы, задайте их по номеру', '+375256208265' ]})

#def news (request):
 #   return render(request, 'mainapp/news.html')

