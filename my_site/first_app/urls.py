from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('<int:page_number>',views.page_num_view),
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view)
]