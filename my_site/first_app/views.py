from django.shortcuts import render  
from django.http.response import HttpResponse,HttpResponseNotFound 


articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

# Create your views here.
def news_view(request, topic):
    try:
        headline = f"<h1>{articles[topic]}</h1>"
        return HttpResponse(headline)
    except:
        headline = "<h1>No article page for that topic!</h1>"
        return HttpResponseNotFound(headline)
        


def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))

