import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import { Table, Container } from 'react-bootstrap'; // Import components from react-bootstrap

function App() {
  const [bookings, setBookings] = useState([]);
  const [sortBy, setSortBy] = useState('checkin');
  const [order, setOrder] = useState('asc');

  useEffect(() => {
    // Fetch bookings from the Django API
    axios
      .get(`http://127.0.0.1:8000/api/bookings-table/?sort_by=${sortBy}&order=${order}`)
      .then((response) => {
        setBookings(response.data);
      })
      .catch((error) => {
        console.error('There was an error fetching the bookings!', error);
      });
  }, [sortBy, order]);

  const handleSortChange = (field) => {
    if (sortBy === field) {
      setOrder(order === 'asc' ? 'desc' : 'asc');
    } else {
      setSortBy(field);
      setOrder('asc');
    }
  };

  const getSortIndicator = (field) => {
    if (sortBy === field) {
      return order === 'asc' ? ' ▲' : ' ▼';
    }
    return '';
  };

  return (
    <Container>
      <h1 className="text-center my-4">Bookings Table</h1>
      <Table striped bordered hover responsive className="my-4">
  <thead>
    <tr>
      <th onClick={() => handleSortChange('flat__name')} style={{ cursor: 'pointer' }}>
        Flat Name {getSortIndicator('flat__name')}
      </th>
      <th>ID</th>
      <th onClick={() => handleSortChange('checkin')} style={{ cursor: 'pointer' }}>
        Check-in {getSortIndicator('checkin')}
      </th>
      <th onClick={() => handleSortChange('checkout')} style={{ cursor: 'pointer' }}>
        Check-out {getSortIndicator('checkout')}
      </th>
      <th>Previous Booking ID</th>
    </tr>
  </thead>
  <tbody>
    {bookings.map((booking) => (
      <tr key={booking.id}>
        <td>{booking.flat.name}</td>
        <td>{booking.id}</td>
        <td>{booking.checkin}</td>
        <td>{booking.checkout}</td>
        <td>{booking.previous_booking_id || '-'}</td>
      </tr>
    ))}
  </tbody>
</Table>

    </Container>
  );
}

export default App;
