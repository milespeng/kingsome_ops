# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [path('polls/latest.html', views.index, name='index'),
               path('admin', admin.site.urls),
               path('<int:question_id>', views.detail, name='detail'),
               path('<int:question_id>/results', views.results, name='results'),
               path('<int:question_id>/vote/', views.vote, name='vote'),

               ]
