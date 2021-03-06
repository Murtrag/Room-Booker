from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from page import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.RoomList.as_view()),
    url("^all_rooms/", views.RoomList.as_view(), name="all_rooms"),
    url(r"^room/new/$", views.AddRoom.as_view(), name="room_new"),
    url(
        r"^room/image/upload/(?P<pk>\d+)$",
        views.UploadImage.as_view(),
        name="room_image_upload",
    ),
    url(
        r"^room/image/remove/$",
        views.DeleteFile.as_view(),
        name="room_image_delete",
    ),
    # url(r"^room/image/upload/$", views.UploadImage.as_view(), name="room_image_upload"),
    url(r"^room/delete/(?P<pk>\d+)$", views.DeleteRoom.as_view(), name="room_delete"),
    url(r"^room/(?P<pk>\d+)", views.DetailRoom.as_view(), name="room_detail"),
    url(
        r"^room/reservation/delete/(?P<pk>\d+)$",
        views.DeleteReservation.as_view(),
        name="reservation_delete",
    ),
    url(r"^room/modify/(?P<pk>\d+)$", views.EditRoom.as_view(), name="room_edit"),
    url(r"^search/", views.SearchView.as_view(), name="search"),
    url(
        r"^reservation/(?P<pk>\d+)", views.ReservationView.as_view(), name="reservation"
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
