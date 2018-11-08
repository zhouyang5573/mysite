from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_title,name='blog_title'),
    path('<int:article_id>/',views.blog_article,name='blog_article'),
    path('encode/',views.test,name = 'test'),
    path('index/',views.index,name = 'test2'),
    path('jsonschema/',views.Schema,name = 'schema'),
    path('json/',views.jsonda,name = 'jsonda'),

]