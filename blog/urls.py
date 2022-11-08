from django.urls import path
from .views import Myview, Post_list, displayTime, greeting, book_list, post_detail ,loginView,profileView,logout_view

app_name = 'blog'

urlpatterns = [
    path("books_list/",book_list, name = "books_list"),
    path("",Post_list),
    path("Contact/",greeting),
    path("about/",Myview.as_view(), name = "home"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
    path("login/",loginView,name="login"),
    path("profile/",profileView,name="profile"),
    path("logout/",logout_view,name="logout"),
]