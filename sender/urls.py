from django.urls import path
from sender.views import ListMail, CreateMail

app_name = 'sender'
urlpatterns = [
    path('', CreateMail.as_view(), name='index'),
    path('list/', ListMail.as_view(), name='list'),
]