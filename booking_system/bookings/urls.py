from django.urls import path
from .views import FlatListView, BookingListView, BookingTableView

urlpatterns = [
    path('flats/', FlatListView.as_view(), name='flat-list'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings-table/', BookingTableView.as_view(), name='booking-table'),
]
