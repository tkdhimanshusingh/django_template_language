from django.urls import path
from . import views
urlpatterns = [
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
    path('date_time/',views.date_time),
]
