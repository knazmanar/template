from django.urls import path
from django.views.generic import TemplateView
from extras import views
urlpatterns = [
    ############### Extras ###############
    # Pages
    path('lockscreen', views.Lockscreen.as_view(),name='lockscreen'),

]