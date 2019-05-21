from django.contrib import admin
from django.urls import path
import blog.views
# from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.layout, name='layout'),
    path('blog/home/', blog.views.home, name='home'),
    path('blog/newblog/', blog.views.blogform, name='newblog'),
    path('blog/create/', blog.views.create, name='create'),
    path('blog/<int:blog_id>/edit/', blog.views.edit, name='edit'),
    path('blog/<int:blog_id>/remove/', blog.views.remove, name='remove'),
    path('blog/<int:blog_id>/detail/', blog.views.detail, name='detail'),
    path('blog/<int:blog_id>/comment_remove/<int:pk>/',blog.views.comment_remove, name='comment_remove'),
    path('blog/<int:blog_id>/comment_edit/<int:pk>/', blog.views.comment_edit, name='comment_edit'),
    # path('',MainpageView.as_view(), name='mainpage'),
]
