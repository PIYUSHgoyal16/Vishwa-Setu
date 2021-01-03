"""Posts URLs"""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from posts import views


urlpatterns = [
    path(
        route='',
        view=login_required(views.PostFeedView.as_view()),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView,
        name='create_post'
    ),

    # path(
    #     route='posts/new/createFromPhoto',
    #     view=views.
    #     name='create_post_fromPhoto'
    # ),

    path(
        route='posts/<int:post_id>/',
        view=login_required(views.PostDetailView.as_view()),
        name='detail'
    ),
]
