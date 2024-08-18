from rest_framework import serializers
from .models import Flat, Booking

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['id', 'name']

class BookingSerializer(serializers.ModelSerializer):
    flat = FlatSerializer()
    previous_booking_id = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'flat', 'checkin', 'checkout', 'previous_booking_id']

    def get_previous_booking_id(self, obj):
        # Get all bookings for the same flat, ordered by checkin date
        previous_bookings = Booking.objects.filter(
            flat=obj.flat,
            checkin__lt=obj.checkin
        ).order_by('-checkin')

        if previous_bookings.exists():
            return previous_bookings.first().id
        return None
