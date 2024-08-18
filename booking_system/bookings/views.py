from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Flat, Booking
from .serializers import FlatSerializer, BookingSerializer

class FlatListView(generics.ListCreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingTableView(APIView):
    def get(self, request):
        # Get sorting parameters from the request
        sort_by = request.GET.get('sort_by', 'flat__name')
        order = request.GET.get('order', 'asc')

        # Adjust sort field based on the order
        if order == 'desc':
            sort_by = f'-{sort_by}'

        # Order the queryset first by flat name, then by check-in date
        bookings = Booking.objects.all().order_by('flat__name', 'checkin')

        # If a different sorting field is provided, apply it
        if sort_by != 'flat__name':
            bookings = bookings.order_by(sort_by, 'flat__name', 'checkin')

        # Serialize and return the sorted data
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
