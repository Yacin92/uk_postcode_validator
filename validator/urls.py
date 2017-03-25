from django.conf.urls import url
from . import views


app_name = 'validator'
urlpatterns = [

    # /validate
    url(r'^validate/', views.validate, name="validate"),

    # /input
    url(r'^input/', views.index, name="index"),

    # /
    url(r'^', views.index, name="index")
]
