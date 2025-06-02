from django.urls import path
from .views import submit_request

urlpatterns = [
    path('', submit_request, name='submit')
]
