from django.urls import path 
from .views import BlogListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='details_post'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('ost/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]