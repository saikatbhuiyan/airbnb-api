from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'rooms'

router = DefaultRouter()
router.register("", views.RoomViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     # path("list/", views.rooms_view),
#     # path("list/", views.ListRoomsView.as_view()),
#     # path("<int:pk>/", views.DetailRoomView.as_view()),
#     path("search/", views.room_search, name="search"),
#     path("", views.RoomsView.as_view()),
#     path("<int:pk>/", views.RoomView.as_view()),
# ]
