from django.conf.urls import url, include
from . import views

# Urls only concerning the Frontend
urlpatterns = [
    url(r'^', views.IndexView.as_view()),
]
