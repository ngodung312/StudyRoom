from django.urls import path
from chat import views 

app_name = 'first_app'

urlpatterns = [
    path(r'', views.main_view, name='main_page'),
]