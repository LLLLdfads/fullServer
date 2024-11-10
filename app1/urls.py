from django.urls import path,include
import app1.views
urlpatterns = [
    path("f1", app1.views.f1),
    path("getInfo", app1.views.getInfo),
]
