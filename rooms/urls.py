from django.urls import path
# from rest_framework.routers import DefaultRouter

from . import views
# from . import viewsets

app_name = 'rooms'

urlpatterns = [
    # path("list/", views.list_rooms),
    path("list/", views.ListRoomsView.as_view()),
    path("<int:pk>/", views.DetailRoomView.as_view()),
]

# router = DefaultRouter()
# router.register("", viewsets.RoomViewset, basename="room")

# urlpatterns = router.urls