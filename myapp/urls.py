from django.urls import path
from .views import home, index, view_name_jon, view_name_jane, view_name, json_view

urlpatterns = [
    path("name/jon/", view_name_jon),
    path("name/jane/", view_name_jane),
    path("get-name/<str:name>/", view_name),

    path('index/', index),
    path('json-view/', json_view),
    path('', home)
]