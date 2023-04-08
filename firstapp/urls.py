from django.urls import path
from firstapp.views import index


urlpatterns = [
    path("home/<int:yosh>",index)
]

