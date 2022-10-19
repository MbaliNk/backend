
from django.urls import path

from .views import Myview, Post_list, displayTime, greeting, book_list, post_detail 

app_name = 'blog'

urlpatterns = [
    path("books_list/",book_list, name = "books_list"),
    path("",Post_list),
    path("Contact/",greeting),
    path("about/",Myview.as_view(), name = "home"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
]