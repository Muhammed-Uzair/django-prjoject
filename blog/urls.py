from django.urls import path, include
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.categ, name='categries'),
    path('posts/', views.home, name='homepage'),
    # path('search/', views.post_search, name='search'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
