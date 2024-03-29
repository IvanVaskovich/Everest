from django.urls import path, include

from .views import *
from .router import *


urlpatterns = [
    path('', include(router.urls)),

    path('posts/<str:slug>/', post_view, name='post'),
]

