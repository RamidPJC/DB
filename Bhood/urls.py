from django.urls import path
from django.views.generic import detail

from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('post/<int:pk>/', post, name='post'),
    path('category/<int:pk>/', detail_cat, name='cat'),
    path('side/', side, name='side'),
    path('add-post/', add_post, name='add-post'),
    path('anim/', anim, name='anim'),
    path('chat/', chat_view, name='chat_view'),
    path('profile/<str:username>/', get_profile, name='get_profile'),
    path('register/', reg, name='register'),
    path('login/', log, name='login'),
    path('logout/', logou, name='logout'),
    path('predlozka/', predl, name='predl'),
    path('predlozka/<int:pk>/', predl_detail, name='predl_detail'),
    path('predlozka/update/<int:pk>/', update_post_from_predl, name='update'),
    path('add-post-admin/', add_post_admin, name='add-post-admin')
]