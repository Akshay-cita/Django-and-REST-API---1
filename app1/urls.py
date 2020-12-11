from django.urls import path

from .views import SongList,SongDetail



urlpatterns = [

	path('<int:pk>/',SongDetail.as_view(),name='songdetail'),
	path('songlist',SongList.as_view(),name='songlist'),

]