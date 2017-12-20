from django.conf.urls import url, include
from django.views.generic import  ListView, DetailView
from mysite.news.models import Articlres

urlpatterns =[
    url(r'^$',
        ListView.as_view(queryset= Articlres.objects.all().order_by("-date")[:20],
        template_name = "news/posts.html")),

]