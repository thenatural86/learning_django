from django.shortcuts import render  
from django.http.response import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def simple_view(request):
    return render(request, 'first_app/example.html')


# articles = {
#     'sports':'Sports Page',
#     'finance':'Finance Page',
#     'politics':'Politics Page'
# }

# # Create your views here.
# def news_view(request, topic):
#     try:
#         headline = f"<h1>{articles[topic]}</h1>"
#         return HttpResponse(headline)
#     except:
#         headline = "<h1>No article page for that topic!</h1>"
#         return HttpResponseNotFound(headline)
        


# def add_view(request, num1, num2):
#     add_result = num1 + num2
#     result = f"{num1} + {num2} = {add_result}"
#     return HttpResponse(str(result))

# pages = ['sports', 'finance', 'politics']

# def page_num_view(request,page_number):
#     # domain.com/first_app/1 ---> domain.com/first_app.finance
#     topic = pages[page_number]
#     return  HttpResponseRedirect(topic)

# def num_page_view(request, num_page):
    
#     topics_list =list(articles.keys())
#     # 'sports', 'finance', 'politics']
#     topic = topics_list[num_page]
    
#     return HttpResponseRedirect(reverse('topic-page', args=[topic]))