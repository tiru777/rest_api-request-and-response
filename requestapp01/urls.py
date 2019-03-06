from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #function based views url
    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    #path('snippets/detail/<int:pk>/', views.snippet_detail),

    #class based views urls
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/detail/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),



]
urlpatterns = format_suffix_patterns(urlpatterns)