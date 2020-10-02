from django.urls import path

from . import views

app_name = 'rooms'

urlpatterns = [
    # path("list/", views.list_rooms),
    path("list/", views.ListRoomsView.as_view()),
    path("<int:pk>/", views.DetailRoomView.as_view()),
]