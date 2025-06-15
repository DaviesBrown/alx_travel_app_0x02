from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint
    path('', views.ListingListCreateAPIView.as_view(), name='listing-list-create'),
]