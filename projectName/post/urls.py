from django.urls import path
from . import views

urlpatterns = [
	path('post', views.ListCreatePostView.as_view()),
 	path('post/<pk>', views.RetrieveUpdateDestroyPostView.as_view() )
]
