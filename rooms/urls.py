from django.urls import path
# from rest_framework.routers import DefaultRouter

from . import views
# from . import viewsets

app_name = 'rooms'

urlpatterns = [
    # path("list/", views.rooms_view),
    # path("list/", views.ListRoomsView.as_view()),
    # path("<int:pk>/", views.DetailRoomView.as_view()),
    path("search/", views.room_search, name="search"),
    path("", views.RoomsView.as_view()),
    path("<int:pk>/", views.RoomView.as_view()),
]

# router = DefaultRouter()
# router.register("", viewsets.RoomViewset, basename="room")

# urlpatterns = router.urls